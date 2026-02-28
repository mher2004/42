#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name, age=0, height=0):
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_age(age)
        self.set_height(height)
    def set_height(self, num):
        if (num<0):
            print(f"Invalid operation attempted: height {num}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = num
            print(f"{self.name}-s height updated {self.__height}cm [OK]")
    def set_age(self, num):
        if (num<0):
            print(f"Invalid operation attempted: age {num} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = num
            print(f"{self.name}-s age updated {self.__age} days [OK]")
    def get_height(self):
        print(f"{self.name}-s height is {self.__height}cm")
    def get_age(self):
        print(f"{self.name}-s age is {self.__age} days")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    aloe = SecurePlant("Aloe")
    aloe.set_age(55)
    aloe.set_age(-455)
    aloe.set_height(55)
    aloe.set_height(-455)
    aloe.get_age()