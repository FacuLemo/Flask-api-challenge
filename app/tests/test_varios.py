import pytest

from app.models.models import Category

def test_category():
    pais= Category(name='Azar')
    assert pais.name=='Azar' #.name='otro' Fallaría
    #assert pais is not None 

def test_inicial():
    assert 1 == 1 # 1==2 fallaría

def test_bool():
    var=False
    assert var is False #mejor que condicional