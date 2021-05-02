import pytest
from multilevel_py.exceptions import ClabjectDeclaredAsInstanceException


def test_animal_has_prop_is_animal(Animal):
    assert hasattr(Animal, "is_animal")


def test_animal_is_animal_is_assigned_to_true(Animal):
    assert Animal.is_animal


def test_tom_props(tom):
    assert tom.name == "tom"
    assert tom.species == "cat"
    assert tom.traits == ["lazy", "food loving"]


def test_jerry_props(jerry):
    assert jerry.name == "jerry"
    assert jerry.species == "mouse"
    assert jerry.traits == ["mischievous", "master mind"]


def test_jerry_is_instance(jerry):
    with pytest.raises(ClabjectDeclaredAsInstanceException):
        # a clabject declared as instanced should not be instantiable any further
        jerry(name="further_clab", init_props={})