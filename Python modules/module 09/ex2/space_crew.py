from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=2, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def custom_validator(self) -> "SpaceMission":
        crew_ranks = [memb.rank for memb in self.crew]
        exp = [memb.years_experience for memb in self.crew]
        active = [memb.is_active for memb in self.crew]
        if self.mission_id[0] != 'M':
            raise ValueError("MissionID must start with M")
        if not (Rank.captain in crew_ranks or Rank.commander in crew_ranks):
            raise ValueError("Missing Captain or Commander")
        if self.duration_days > 365:
            if sum([1 if i > 5 else 0 for i in exp])/len(exp) < 0.5:
                raise ValueError(" Long missions (> 365 days) need 50%\
 experienced crew (5+ years)")
        if sum(active) < len(self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 45)
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Mission",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=200,
            budget_millions=500,

            crew=[
                CrewMember(
                    member_id="C111",
                    name="John",
                    rank=Rank.commander,
                    age=40,
                    specialization="Pilot",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C200",
                    name="Alice",
                    rank=Rank.officer,
                    age=35,
                    specialization="Engineer",
                    years_experience=6,
                    is_active=True
                )
            ]
        )
        print("Space Mission Crew Validation")
        print("=" * 41)

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")

        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})\
 - {member.specialization}")

    except ValidationError as e:
        print(e)

    print("=" * 45)
    try:
        SpaceMission(
            mission_id="X123",
            mission_name="Bad ID Mission",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=100,
            budget_millions=200,
            crew=[
                CrewMember(
                    member_id="C12",
                    name="John",
                    rank=Rank.commander,
                    age=40,
                    specialization="Pilot",
                    years_experience=10,
                    is_active=True
                )
            ]
        )
    except ValidationError as e:
        print("ID error:", e.errors()[0]["msg"])

    try:
        SpaceMission(
            mission_id="M12345",
            mission_name="No Leader",
            destination="Moon",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=100,
            budget_millions=200,
            crew=[
                CrewMember(
                    member_id="C13",
                    name="Bob",
                    rank=Rank.officer,
                    age=30,
                    specialization="Tech",
                    years_experience=4,
                    is_active=True
                )
            ]
        )
    except ValidationError as e:
        print("Rank error:", e.errors()[0]["msg"])

    try:
        SpaceMission(
            mission_id="M99999",
            mission_name="Long Mission",
            destination="Jupiter",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=500,
            budget_millions=800,
            crew=[
                CrewMember(
                    member_id="C14",
                    name="Tom",
                    rank=Rank.commander,
                    age=40,
                    specialization="Pilot",
                    years_experience=2,
                    is_active=True
                ),
                CrewMember(
                    member_id="C25",
                    name="Jerry",
                    rank=Rank.officer,
                    age=35,
                    specialization="Engineer",
                    years_experience=1,
                    is_active=True
                )
            ]
        )
    except ValidationError as e:
        print("Experience error:", e.errors()[0]["msg"])

    try:
        SpaceMission(
            mission_id="M77777",
            mission_name="Inactive Crew",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 12, 0, 0),
            duration_days=100,
            budget_millions=300,
            crew=[
                CrewMember(
                    member_id="C14",
                    name="John",
                    rank=Rank.commander,
                    age=40,
                    specialization="Pilot",
                    years_experience=10,
                    is_active=False
                )
            ]
        )
    except ValidationError as e:
        print(" Active error:", e.errors()[0]["msg"])


main()
