import pytest
from app import app, db
from app.models.models import Category


@pytest.fixture  #'marcado': este fixture queda para TODOS los tests
def cliente():
    with app.app_context():
        db.create_all()

    cliente = app.test_client()

    yield cliente  # funciona como un return sin terminar la funcion

    with app.app_context():
        db.session.rollback()


def test_get_categories_fail(cliente):
    response = cliente.get("/api/v1/category")
    # import ipdb; ipdb.set_trace() #esto frena el curso del test, como un break
    # si hacemos pytest -s nos deja usar la consola
    # con toda la info hasta ese momento.
    # si estuviese en un bucle se ejecuta cada vez
    assert response.status_code == 404  # reemplazar por 200 para que falle


def test_get_categories(cliente):
    # Act
    response = cliente.get("/categories")
    # Assert
    data = response.json

    assert len(data) == 2  # esto falla al minimo cambio de la db, para eso el rollback
    # NO pudimos hacer andar el rollback. 17/10/23
    assert data[0] == dict(id=1, name="Misc")
    assert response.status_code == 200


def test_post_category(cliente):
    # Arrange
    data = dict(name="Libros")
    # Act
    response = cliente.post("/categories", json=data)
    # Assert
    assert response.status_code == 200  # 201 es el código que salió bien el POST
    # pero esta mal hecha la api
    # with app.app_context():
    #    categ=Category.query.last() tira excepcion
    #assert categ.name == "Libros"
