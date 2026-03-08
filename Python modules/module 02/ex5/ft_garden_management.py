class GardenError(Exception):
    '''Exception for Garden class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught GardenError:\n" + message
        else:
            self.message = "Caught GardenError:\n"
        print(self.message)


class PlantError(GardenError):
    '''Exception for Plant class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught PlantError:\n" + message
        else:
            self.message = "Caught PlantError:\n"
        print(self.message)


class WaterError(GardenError):
    '''Exception for Water class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught WaterError:\n" + message
        else:
            self.message = "Caught WaterError:\n"
        print(self.message)


class GardenManager:
    def __init__(self, tank_water: int) -> None:
        self.garden = {}
        try:
            self.__tank = int(tank_water)
        except TypeError:
            print("Wrong input for water tank")
            self.__tank = 0

    def check_tank(self) -> None:
        try:
            if self.__tank == 0:
                raise GardenError("Not enough water in tank")
        except GardenError:
            print("Please full the tank with the \
method full_tank() for continuing...")
        else:
            print("System working as expected")

    def add_plant(self, name: str, watered_days: int, sun: int) -> None:
        try:
            if name is None:
                raise PlantError("Undefined name format")
            int(watered_days)
            int(sun)
        except PlantError:
            print("Please enter valid name")
        except TypeError:
            print("Please enter valid number")
        else:
            print(f"Added {name} successfully!")
            self.garden[name] = [watered_days, sun]

    def water_plants(self) -> None:
        print("Watering plants...")
        try:
            for plant in self.garden.keys():
                if self.__tank == 0:
                    raise WaterError("No enough water in the tank")
                self.garden[plant][0] = 0
                self.__tank -= 1
                print(f"Watering {plant}")
        except WaterError:
            print("Please full the tank with the method full_tank()")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.garden.keys():
            try:
                if self.garden[plant][0] > 10:
                    raise PlantError(f"Error checking {plant}:\
 Water level {self.garden[plant][0]} is too high (max 10)")
                if self.garden[plant][1] > 12 or self.garden[plant][1] < 4:
                    raise PlantError(f"Error checking {plant}:\
 Sunlight level {self.garden[plant][1]} is too high (max 12, min 4)")
            except PlantError:
                pass
            else:
                print(f"{plant}: healthy \
(water: {self.garden[plant][0]},sun:{self.garden[plant][1]})")

    def full_tank(self, num: int) -> None:
        try:
            self.__tank += int(num)
        except TypeError:
            print("Wrong input for water tank")
        else:
            print("Tank fulled successfully")


def test_garden_managment() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager(None)
    garden.add_plant("tomatoes", 5, 5)
    garden.add_plant(None, 1, 2)
    garden.add_plant('Banjar', 10, 5)
    garden.add_plant("aloe", 15, 5)
    garden.add_plant("cactus", 8, 50)

    print()
    garden.water_plants()

    print("\nChecking plant health...")
    garden.check_plant_health()

    print("\nTesting error recovery...")
    garden.check_tank()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_managment()
