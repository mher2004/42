#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.age = age
        self.name = name
        self.height = height


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} bloom")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} shadeee")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    rose = Flower("Rose", 30, 10, "Red")
    lily = Flower("Lily", 25, 5, "White")

    oak = Tree("Oak", 500, 3650, 120)
    pine = Tree("Pine", 300, 1500, 45)

    carrot = Vegetable("Carrot", 15, 60, "Autumn", "Vitamin A")
    kale = Vegetable("Kale", 20, 45, "Winter", "Iron")

    rose.bloom()
    oak.produce_shade()
    print(f"The {carrot.name} is high in {carrot.nutritional_value}.")
