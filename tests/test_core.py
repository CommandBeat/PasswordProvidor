# test_core.py

from PasswordProvidor import generator

def test_with_blank():
    assert generator.Generator() == True
