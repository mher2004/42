#!/usr/bin/env python3
def check_temperature(temp_str: str) -> int:
    try:
        txt = "Error: " + temp_str + " is not a valid number"
        a = int(temp_str)
        if a > 40:
            txt = "Error: " + temp_str + " is too \
hot for plants (max 40°C)"
            raise ValueError(txt)
        elif a < 0:
            txt = "Error: " + temp_str + " is too \
cold for plants (min 0°C)"
            raise ValueError(txt)
    except ValueError:
        print(txt)
    else:
        print(f"Temperature {a}°C is perfect for plants!")
        return a


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


test_temperature_input()
