from multilevel_py.constraints import is_str_constraint
from multilevel_py.clabject_prop import CollectionDescription
from multilevel_py.core import create_clabject_prop, Clabject, MetaClabject

Animal = Clabject(name="Animal")

# Declare Properties to be instantiated down the classification hierarchy
is_animal = create_clabject_prop(n="is_animal", t=0, f="*", v=True)
species = create_clabject_prop(n="species", t=1, f='*', c=[is_str_constraint])
name = create_clabject_prop(n="name", t=2, f='*', c=[is_str_constraint])
traits = create_clabject_prop(n="traits", t=2, f='*', coll_desc=(1,3, is_str_constraint))
Animal.define_props([is_animal, species, name, traits])

def create_tom(animal_clabject):
    """Create a 'clabject' representing the cartoon character Tom

    Parameters
    ----------
    animal_clabject : multilevel_py.core.MetaClabject
        the Animal clabject, i.e. the top of the classification hierarchy defined above

    Returns
    -------
    multilevel_py.core.MetaClabject
        the tom clabject (declared as instance)
    """
    Cat = animal_clabject(name="Cat", init_props={"species": "cat"})
    return Cat(name="tom", init_props={"name": "tom", "traits": ["lazy", "food loving"]}, declare_as_instance=True)

def create_jerry(animal_clabject):
    """Create a 'clabject' representing the cartoon character Jerry

    Parameters
    ----------
    animal_clabject : multilevel_py.core.MetaClabject
        the Animal clabject, i.e. the top of the classification hierarchy defined above

    Returns
    -------
    multilevel_py.core.MetaClabject
        the jerry clabject (declared as instance)
    """
    Mouse = animal_clabject(name="Mouse", init_props={"species": "mouse"})
    return Mouse(name="jerry", init_props={"name": "jerry", "traits": ["mischievous", "master mind"]}, declare_as_instance=True)
