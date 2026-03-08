def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if plant_name is None:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10 or water_level < 1:
        raise ValueError(f"Error: Water level {water_level}\
 is too high (max 10)")
    elif sunlight_hours > 12 or sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}\
 is too low (min 2)")
    return f"Plant {plant_name} is healthy!"


def test_plant_checks() -> None:
    print("Testing good values...")
    print(check_plant_health("aloe", 5, 7))
    try:
        print("\nTesting empty plant name...")
        print(check_plant_health(None, 5, 7))
    except ValueError as txt:
        print(txt)
    try:
        print("\nTesting bad water level...")
        print(check_plant_health("aloe", 50, 7))
    except ValueError as txt:
        print(txt)
    try:
        print("\nTesting bad sunlight hours...")
        print(check_plant_health("aloe", 5, 70))
    except ValueError as txt:
        print(txt)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
