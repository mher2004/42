#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.start_height = height
        self.starting_age = age
        self.actual_age = age
        self.actual_height = height
        print(f"Created: {self.name}: {self.actual_height}cm,\
{self.actual_age} days old")

    def get_info(self) -> None:
        print(f"{self.name}: {self.actual_height}cm,\
{self.actual_age} days old")

    def grow(self, num: int) -> None:
        self.actual_height += num

    def age(self, num: int) -> None:
        self.actual_age += num

    def get_week_change(self) -> None:
        print(f"Growth of {self.name} this week: +\
{self.actual_height-self.start_height}cm")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Fern", 10, 5),
        ("Cactus", 5, 20),
        ("Oak", 50, 100),
        ("Rose", 15, 12),
        ("Bamboo", 100, 30)]
    garden = [Plant(n, h, a) for n, h, a in plant_data]
    for plant in garden:
        plant.age(7)
        plant.grow(2)
    for plant in garden:
        plant.get_info()
    for plant in garden:
        plant.get_week_change()
    print(f"Total plants created: {len(garden)}")
