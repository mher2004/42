from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_validator(self) -> "AlienContact":
        if self.contact_id[:2] != 'AC':
            raise ValueError("ContactID must start with AC")
        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError("When contact type is physical\
 is_verified must be True")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError("When contact type is telepathic\
 witness_count must be >=3")
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("When signal_strength is >7.0\
 message_received must be not None")
        return self


def main() -> None:
    print("Alien Contact Data Validation")
    print("=" * 40)
    alien = AlienContact(
        contact_id="AC4744",
        timestamp=datetime(2024, 1, 1, 12, 0, 0),
        location="somewhere",
        contact_type=ContactType.radio,
        signal_strength=5,
        duration_minutes=122,
        witness_count=55,
        message_received="qwertyuytrew",
        is_verified=False,
        )
    print("Valid alien contact created:")
    print("ID:", alien.contact_id)
    print("timestamp:", alien.timestamp)
    print("location:", alien.location)
    print("contact_type:", alien.contact_type.value)
    print("signal_strength:", alien.signal_strength)
    print("duration_minutes:", alien.duration_minutes)
    print("witness_count:", alien.witness_count)
    print("message_received:", alien.message_received)
    print("is_verified:", alien.is_verified)
    print("=" * 40)

    try:
        alien = AlienContact(
            contact_id="AC4744",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            location="somewhere",
            contact_type=ContactType.telepathic,
            signal_strength=5,
            duration_minutes=122,
            witness_count=2,
            message_received="qwertyuytrew",
            is_verified=False,
            )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])
    print("=" * 40)
    try:
        alien = AlienContact(
            contact_id="AG4744",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            location="somewhere",
            contact_type=ContactType.telepathic,
            signal_strength=5,
            duration_minutes=122,
            witness_count=2,
            message_received="qwertyuytrew",
            is_verified=False,
            )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])
    print("=" * 40)
    try:
        alien = AlienContact(
            contact_id="AC4744",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            location="somewhere",
            contact_type=ContactType.physical,
            signal_strength=5,
            duration_minutes=122,
            witness_count=2,
            message_received="qwertyuytrew",
            is_verified=False,
            )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])
    print("=" * 40)
    try:
        alien = AlienContact(
            contact_id="AC4744",
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
            location="somewhere",
            contact_type=ContactType.physical,
            signal_strength=8,
            duration_minutes=122,
            witness_count=2,
            is_verified=True,
            )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])
    print("=" * 40)


main()
