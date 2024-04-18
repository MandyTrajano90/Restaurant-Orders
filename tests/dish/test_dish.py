from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Lasanha", 25.0)
    dish2 = Dish("Lasanha", 25.0)

    assert dish1.name == "Lasanha"
    assert dish1.price == 25.00
    assert dish1.recipe == {}

    assert dish1 == dish2

    assert hash(dish1) == hash("Dish('Lasanha', R$25.00)")

    assert repr(dish1) == "Dish('Lasanha', R$25.00)"

    ingredient = Ingredient("salsinha")

    assert dish1.add_ingredient_dependency(ingredient, 10) is None

    assert dish1.recipe == {Ingredient('salsinha'): 10}

    assert dish1.get_ingredients() == {ingredient}

    assert dish1.get_restrictions() == set()

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Minestrone", "10")

    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
    ):
        Dish("Minestrone", 0)
