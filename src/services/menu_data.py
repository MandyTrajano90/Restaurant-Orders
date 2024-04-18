import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.menu(source_path)

    def menu(self, source_path: str) -> None:
        with open(source_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                dish_name, price, ingredient_name, quantity = row
                ct_dish = self.get_new_dish(dish_name)

                if ct_dish is None:
                    ct_dish = Dish(dish_name, float(price))
                    self.dishes.add(ct_dish)

                ingredient = Ingredient(ingredient_name)
                ct_dish.add_ingredient_dependency(ingredient, int(quantity))

    def get_new_dish(self, dish_name: str):
        for new_dish in self.dishes:
            if new_dish.name == dish_name:
                return new_dish
        return None
