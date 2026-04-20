from pydantic import BaseModel, Field, model_validator, ValidationError
from pydantic import field_validator
from enum import Enum
from typing import Any, Tuple, Optional
from errors import LineFormatError, ConfigFormatError

CONFIG = "config.txt"


class Color(Enum):
    yellow = 33
    blue = 34
    white = 37


class Config(BaseModel):
    width: int = Field(..., ge=1)
    height: int = Field(..., ge=1)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    # entryx: int = Field(..., ge=0)
    # entryy: int = Field(..., ge=0)
    # exitx: int = Field(..., ge=0)
    # exity: int = Field(..., ge=0)
    output_file: str = Field(..., min_length=1)
    perfect: bool
    seed: Optional[str] = Field(..., min_length=1)
    Color: Any = Color.white
    model_config = {"validate_assignment": True}

    @field_validator("Color", mode="before")
    @classmethod
    def parse_Color(cls, value):
        if value is None:
            return Color.white
        try:
            return Color[value.lower()]
        except KeyError:
            print(f"Invalid Color key value '{value}'")
            print("Choose from: yellow, blue, white")
            # print("Color set to the default - white")
            # return Color.white
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
        # if self.perfect is not True and self.perfect is not False:
        #     raise LineFormatError(f"Value of PERFECT '{self.perfect}' " +
        #                           "is niether True, nor False")
        return self


class ConfigFields(Enum):
    width = "WIDTH"
    height = "HEIGHT"
    entry = "ENTRY"
    exit = "EXIT"
    output_file = "OUTPUT_FILE"
    perfect = "PERFECT"
    seed = "SEED"
    color = "Color"


class Line(BaseModel):
    field: ConfigFields
    value: Any


def parce_lines(f) -> list:
    raw_lines = [line.strip() for line in f.readlines()
                 if not line.lstrip().startswith("#") and line.strip()]
    # print(raw_lines)
    form_lines = list()
    for line in raw_lines:
        splited = line.split("=")
        # print("splited =", splited)
        if len(splited) != 2:
            # print(f"len = {len(splited)}")
            raise LineFormatError(f"Invalid config line '{line}' format")
        if splited[0].upper() != splited[0]:
            # print(f"key = {splited[0]}")
            raise LineFormatError(f"Key '{splited[0]}' is not uppercase!")
            # print("passed 1")
        form_lines.append(Line(
            field=ConfigFields[splited[0].lower()],
            value=splited[1])
        )
        # print("done iter")
    # print("done cycle")
    return form_lines


def get_init(lines) -> dict:
    res = dict()
    for field in ConfigFields:
        res[field.name] = None
    # print(lines)
    # print("1")
    for line in lines:
        if res[line.field.name]:
            raise ConfigFormatError(
                f"Repeated config key '{line.field.name}'!")
        # print("2")
        res[line.field.name] = line.value
        # print("3")
    # print(res)
    return res


def parce() -> Config | None:
    try:
        with open(CONFIG, "r") as f:
            lines = parce_lines(f)
            if len(lines) < 5:
                raise ConfigFormatError("Excessive line!")
            init_dict = get_init(lines)
            # print(init_dict)
            config = Config(**init_dict)
            return config
    except FileNotFoundError:
        print("Config file (config.txt) not found!")
        return None
    except PermissionError:
        print("No read permission to config file (config.txt)!")
        return None
    except ConfigFormatError as e:
        print(e)
        return None
    except ValidationError as e:
        print("Validation error:", e)
        return None
