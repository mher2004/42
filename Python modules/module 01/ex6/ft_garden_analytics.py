#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def __repr__(self):
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color, bloom):
        super().__init__(name, height)
        self.color = color
        self.bloom = bloom

    def __repr__(self):
        if self.bloom:
            return (f"- {self.name}: {self.height}cm, {self.color} (blooming)")
        else:
            return (f"- {self.name}: {self.height}cm, {self.color}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, bloom, points):
        super().__init__(name, height, color, bloom)
        self.points = points

    def __repr__(self):
        if self.bloom:
            return (f"- {self.name}: {self.height}cm, {self.color}\
 (blooming), Prize points: {self.points}")
        else:
            return (f"- {self.name}: {self.height}cm, {self.color}\
, Prize points: {self.points}")


class GardenManager:
    def __init__(self):
        self.garden = {}

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def type_count(self):
            plants = 0
            flower_plant = 0
            prize_plant = 0
            for plant in self.garden:
                if isinstance(plant, PrizeFlower):
                    prize_plant += 1
                elif isinstance(plant, FloweringPlant):
                    flower_plant += 1
                else:
                    plants += 1
            print(f"Plant types: {plants} regular, {flower_plant} flowering,\
 {prize_plant} prize flowers")

        def stats(self):
            growth = 0
            count = 0
            for plant in self.garden:
                growth += plant.growth
                count += 1
            print(f"Plants added: {count}, Total growth: {growth}cm")

    def add_plant(self, garden_name, plant):
        self.garden[garden_name].append(plant)
        print(f"Added {plant.name} to {garden_name}'s garden")

    def help_all_grow(self, garden_name):
        print(f"{garden_name} is helping all plants grow...")
        for plant in self.garden[garden_name]:
            plant.grow()

    def print_report(self, garden_name):
        print(f"=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden[garden_name]:
            print(plant)
        print()
        stat = self.GardenStats(self.garden[garden_name])
        stat.stats()
        stat.type_count()

    def score(self):
        print("Garden scores - ", end="")
        i = 0
        for garden in self.garden.keys():
            total_score = 0
            for plant in self.garden[garden]:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.height
                    total_score += plant.bloom * 15
                    total_score += plant.points
                elif isinstance(plant, FloweringPlant):
                    total_score += plant.height
                    total_score += plant.bloom * 15
                else:
                    total_score += plant.height
            i += 1
            print(f"{garden}: {total_score}", end="")
            if (i != len(self.garden)):
                print(", ", end="")
        print()
        print("Total gardens managed:", i)

    @staticmethod
    def validate_height(value):
        return True if value >= 0 else False

    @classmethod
    def create_garden_network(cls):
        print("=== Garden Management System Demo ===\n")
        manager = cls()
        manager.garden["Alice"] = []
        manager.garden["Bob"] = [Plant("Cactus", 92)]
        manager.add_plant("Alice", Plant("Oak Tree", 100))
        manager.add_plant("Alice", FloweringPlant("Rose", 25,
                                                  "red flowers", 1))
        manager.add_plant("Alice", PrizeFlower("Sunflower",
                                               50, "yellow flowers", 1, 10))
        print()
        manager.help_all_grow("Alice")
        print()
        manager.print_report("Alice")
        print()
        print("Height validation test: ", manager.validate_height(55))
        manager.score()
        return manager


if __name__ == "__main__":
    testing = GardenManager().create_garden_network()
    # GardenManager.create_garden_network()
    # print()
    # testing.help_all_grow("Alice")
    # testing.score()
