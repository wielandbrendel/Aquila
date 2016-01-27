from mock import Mock
import pytest

class TestRecipe:

    @pytest.fixture
    def recipe(self):
        from aquila.recipes.base import Recipe
        return Recipe('key')

    def test_get_canvas_on_first(self, recipe):
        assert recipe.get_canvas() == recipe.canvas

    def test_get_canvas_on_second(self, recipe):
        from aquila.recipes.base import Recipe
        recipe_second = Recipe('key2', canvas=recipe)
        assert recipe_second.get_canvas() == recipe.get_canvas()

    def test_get_canvas_from_fig(self, recipe):
        from aquila.recipes.base import Recipe
        recipe_second = Recipe('key2', canvas=recipe.canvas)
        assert recipe_second.get_canvas() == recipe.get_canvas()

    def test_update_not_implemented(self, recipe):
        with pytest.raises(NotImplementedError):
            recipe.update(Mock())

