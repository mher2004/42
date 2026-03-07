def water_plants(plant_list):
    print("Testing normal watering...")
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


def test_watering_system():
    water_plants(['tomatoes', 'lettuce', 'carrots'])
    water_plants(['apples', 4])
    water_plants(['oranges', None])


test_watering_system()
