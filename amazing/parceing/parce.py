from pydantic import BaseModel, Field, model_validator, ValidationError
from pydantic import field_validator
from enum import Enum
from typing import Any, Tuple, Optional
from errors import LineFormatError, ConfigFormatError
from io import TextIOWrapper


class Color(Enum):
    yellow = 33
    blue = 34
    white = 37


class Config(BaseModel):
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str = Field(..., min_length=1)
    perfect: bool
    seed: Optional[str] = Field(..., min_length=1)
    color: Any[Color, str] = Color.white
    is_ft: bool = True
    model_config = {"validate_assignment": True}

    @field_validator("color", mode="before")
    @classmethod
    def parse_Color(cls, value: str) -> Enum:
        if value is None:
            return Color.white
        try:
            return Color[value.lower()]
        except KeyError:
            print(f"Invalid Color key value '{value}'")
            print("Choose from: yellow, blue, white")
            raise LineFormatError(f"Invalid Color '{value}'")

    @field_validator("entry", "exit", mode="before")
    @classmethod
    def parse_entry(cls, value: str) -> tuple:
        splited = value.split(",")
        if len(splited) != 2:
            raise LineFormatError("Wrong ENTRY value format!")
        return (int(splited[0]), int(splited[1]))

    @model_validator(mode="after")
    def val_cont_rules(self) -> "Config":
        if self.entry[0] < 0 or self.entry[1] < 0:
            raise LineFormatError("some ENTRY coordinat is negative!")
        if self.exit[0] < 0 or self.exit[1] < 0:
            raise LineFormatError("some EXIT coordinat is negative!")
        if self.entry[0] >= self.width or self.entry[1] >= self.height:
            raise LineFormatError("some ENTRY coordinat is " +
                                  "too big and out of border!")
        if self.exit[0] >= self.width or self.exit[1] >= self.height:
            raise LineFormatError("some EXIT coordinat is " +
                                  "too big and out of border!")
        if self.exit[0] == self.entry[0] and self.exit[1] == self.entry[1]:
            raise ConfigFormatError("ENTRY and EXIT overlap!")
        return self


class ConfigFields(Enum):
    width = "WIDTH"
    height = "HEIGHT"
    entry = "ENTRY"
    exit = "EXIT"
    output_file = "OUTPUT_FILE"
    perfect = "PERFECT"
    seed = "SEED"
    color = "COLOR"


class Line(BaseModel):
    field: ConfigFields
    value: Any


def parce_lines(f: TextIOWrapper) -> list:
    raw_lines = [line.strip() for line in f.readlines()
                 if not line.lstrip().startswith("#") and line.strip()]
    form_lines = list()
    for line in raw_lines:
        splited = line.split("=")
        if len(splited) != 2:
            raise LineFormatError(f"Invalid config line '{line}' format")
        if splited[0].upper() != splited[0]:
            raise LineFormatError(f"Key '{splited[0]}' is not uppercase!")
        try:
            form_lines.append(Line(
                field=ConfigFields[splited[0].lower()],
                value=splited[1])
            )
        except KeyError:
            raise ConfigFormatError(f"Key {splited[0]} is not accepted!")
    return form_lines


def get_init(lines: list) -> dict:
    res: dict[Any, Any] = dict()
    for field in ConfigFields:
        res[field.name] = None
    for line in lines:
        if res[line.field.name]:
            raise ConfigFormatError(
                f"Repeated config key '{line.field.name}'!")
        res[line.field.name] = line.value
    return res


def parce(config_file: str) -> Config | None:
    res = None
    try:
        with open(config_file, "r") as f:
            lines = parce_lines(f)
            if len(lines) < 5:
                raise ConfigFormatError("Excessive line!")
            init_dict = get_init(lines)
            config = Config(**init_dict)
            if config.width < 9 or config.height < 7:
                config.is_ft = False
            try:
                with open(config.output_file, "w") as _:
                    pass
            except PermissionError:
                print("No write permission to " +
                      f"config file {config.output_file}!")
            res = config
    except FileNotFoundError:
        print(f"Config file {config_file} not found!")
    except PermissionError:
        print(f"No read permission to config file {config_file}!")
    except ConfigFormatError as e:
        print(e)
    except ValidationError as e:
        print("Validation error:", e)
    return res
