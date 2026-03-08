class GardenError(Exception):
    '''Exception for Garden class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught GardenError: " + message
        else:
            self.message = "Caught GardenError: "
        print(self.message)


class PlantError(GardenError):
    '''Exception for Plant class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught PlantError: " + message
        else:
            self.message = "Caught PlantError: "
        print(self.message)


class WaterError(GardenError):
    '''Exception for Water class'''
    def __init__(self, message: str = None) -> None:
        if message is not None:
            self.message = "Caught WaterError: " + message
        else:
            self.message = "Caught WaterError: "
        print(self.message)


def testing_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato is wiling!\n")
    except PlantError:
        pass
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!\n")
    except WaterError:
        pass
    try:
        print("Testing catching all garden errors...")
        raise GardenError("The tomato is wiling!")
    except GardenError:
        pass
    try:
        raise GardenError("Not enough water in the tank!\n")
    except GardenError:
        pass
        print("All custom error types work correctly!")


testing_errors()
