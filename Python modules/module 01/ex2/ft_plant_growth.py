#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.start_height = height
        self.agee = age
        self.actual_height = height

    def get_info(self) -> None:
        print(f"{self.name}: {self.actual_height}cm, {self.agee} days old")

    def grow(self, num: int) -> None:
        self.actual_height += num

    def age(self, num: int) -> None:
        self.agee += num

    def get_week_change(self) -> None:
        print(f"Growth of {self.name} this week: +\
{self.actual_height-self.start_height}cm")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    aloe = Plant("Aloe", 21, 26)
    cactus = Plant("Cactus", 52, 200)
    jade = Plant("Jade", 60, 100)
    for i in range(1, 8):
        print(f"===Day {i} ===")
        aloe.grow(1)
        aloe.age(1)
        cactus.grow(1)
        cactus.age(1)
        jade.grow(1)
        jade.age(1)
        aloe.get_info()
        cactus.get_info()
        jade.get_info()
    aloe.get_week_change()
    cactus.get_week_change()
    jade.get_week_change()
