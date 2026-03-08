def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    a = ''
    b = 1
    try:
        for i in plant_list:
            txt = "Watering "
            a = i
            print(txt + i)
    except TypeError:
        print(f"Error: Cannot water {a} - invalid plant!")
        b = 0
    finally:
        print("Closing watering system (cleanup)")
        if b:
            print("Watering completed successfully!\n")
        else:
            print()


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(['tomatoes', 'lettuce', 'carrots'])
    print("Testing with error...")
    water_plants(['apples', 4])
    water_plants(['oranges', None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
