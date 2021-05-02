"""
entry-point functions for the sample_pck module, as referenced in setup.cfg 
"""

from .animals import Animal, create_jerry, create_tom

def main() -> tuple:
    tom = create_tom(Animal)
    jerry = create_jerry(Animal)
    return (tom, jerry)