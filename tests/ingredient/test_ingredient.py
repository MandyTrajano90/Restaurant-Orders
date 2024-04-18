from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("salsinha")
    ingredient2 = Ingredient("salsinha")

    assert ingredient1.name == "salsinha"
    assert ingredient1.restrictions == set()

    assert hash(ingredient1) == hash("salsinha")

    assert ingredient1 == ingredient2

    assert repr(ingredient1) == "Ingredient('salsinha')"
