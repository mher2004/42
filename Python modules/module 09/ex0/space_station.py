from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 1, 12, 0, 0)
    )
    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew:", station.crew_size, "people")
    print("Power:", station.power_level, "%")
    print("Oxygen:", station.oxygen_level, "%")
    print("Status:",
          "Operational" if station.is_operational else "Nonoperational")
    print("=" * 40)
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 1, 12, 0, 0)
        )
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print("Crew:", station.crew_size)
        print("Power:", station.power_level)
        print("Oxygen:", station.oxygen_level)
        print("Status:",
              "Operational" if station.is_operational else "Nonoperational")
        print("=" * 40)
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])


main()
