#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, age: int = 0, height: int = 0) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_age(age)
        self.set_height(height)

    def set_height(self, num: int) -> None:
        if (num < 0):
            print(f"Invalid operation attempted: height {num}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = num
            print(f"{self.name}-s height updated {self.__height}cm [OK]")

    def set_age(self, num: int) -> None:
        if (num < 0):
            print(f"Invalid operation attempted: age {num} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = num
            print(f"{self.name}-s age updated {self.__age} days [OK]")

    def get_height(self) -> None:
        print(f"{self.name}-s height is {self.__height}cm")

    def get_age(self) -> None:
        print(f"{self.name}-s age is {self.__age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    aloe = SecurePlant("Aloe")
    aloe.set_age(55)
    aloe.set_age(-455)
    aloe.set_height(55)
    aloe.set_height(-455)
    aloe.get_age()
