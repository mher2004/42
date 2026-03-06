#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        self.__height = height
        self.__growth = 0

    def grow(self) -> None:
        self.__height += 1
        self.__growth += 1
        print(f"{self.__name} grew 1cm")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_growth(self) -> int:
        return self.__growth

    def __repr__(self) -> str:
        return (f"- {self.__name}: {self.__height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str,
                 bloom: bool) -> None:
        super().__init__(name, height)
        self.__color = color
        self.__bloom = bloom

    def get_color(self) -> str:
        return self.__color

    def get_bloom(self) -> bool:
        return self.__bloom

    def __repr__(self) -> str:
        if self.__bloom:
            return (f"- {self.get_name()}: {self.get_height()}cm,\
 {self.get_color()} (blooming)")
        else:
            return (f"- {self.get_name()}: {self.get_height()}cm,\
 {self.get_color()}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, bloom: bool, points: int) -> None:
        super().__init__(name, height, color, bloom)
        self.__points = points

    def get_points(self) -> int:
        return self.__points

    def __repr__(self) -> str:
        if self.get_bloom():
            return (f"- {self.get_name()}: {self.get_height()}cm,\
 {self.get_color()} (blooming), Prize points: {self.get_points()}")
        else:
            return (f"- {self.get_name()}: {self.get_height()}cm,\
{self.get_color()}, Prize points: {self.get_points()}")


class GardenManager:
    def __init__(self) -> None:
        self.garden = {}

    class GardenStats:
        def __init__(self, garden: 'GardenManager') -> None:
            self.garden = garden

        def type_count(self) -> None:
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

        def stats(self) -> None:
            growth = 0
            count = 0
            for plant in self.garden:
                growth += plant.get_growth()
                count += 1
            print(f"Plants added: {count}, Total growth: {growth}cm")

    def add_plant(self, garden_name: str, plant: Plant) -> None:
        self.garden[garden_name].append(plant)
        print(f"Added {plant.get_name()} to {garden_name}'s garden")

    def help_all_grow(self, garden_name: str) -> None:
        print(f"{garden_name} is helping all plants grow...")
        for plant in self.garden[garden_name]:
            plant.grow()

    def print_report(self, garden_name: str) -> None:
        print(f"=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden[garden_name]:
            print(plant)
        print()
        stat = self.GardenStats(self.garden[garden_name])
        stat.stats()
        stat.type_count()

    def score(self) -> None:
        print("Garden scores - ", end="")
        i = 0
        for garden in self.garden.keys():
            total_score = 0
            for plant in self.garden[garden]:
                if isinstance(plant, PrizeFlower):
                    total_score += plant.get_height()
                    total_score += plant.get_bloom() * 15
                    total_score += plant.get_points()
                elif isinstance(plant, FloweringPlant):
                    total_score += plant.get_height()
                    total_score += plant.get_bloom() * 15
                else:
                    total_score += plant.get_height()
            i += 1
            print(f"{garden}: {total_score}", end="")
            if (i != len(self.garden)):
                print(", ", end="")
        print()
        print("Total gardens managed:", i)

    @staticmethod
    def validate_height(value: int) -> bool:
        return True if value >= 0 else False

    @classmethod
    def create_garden_network(cls: 'GardenManager') -> 'GardenManager':
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
