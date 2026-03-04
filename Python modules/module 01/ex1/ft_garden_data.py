#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def see(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    aloe = Plant("Aloe", 21, 26)
    cactus = Plant("Cactus", 52, 200)
    jade = Plant("Jade", 60, 100)
    aloe.see()
    cactus.see()
    jade.see()
