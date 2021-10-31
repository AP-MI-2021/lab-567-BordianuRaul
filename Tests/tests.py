from Domain.object import get_new_object, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'IKEA')
    ]


def test_create():

    lista = get_data()
    new_object = get_new_object(6, 'minge', 'baschet', 25, 'AMNR')
    lista_noua = create(lista, 6, 'minge', 'baschet', 25, 'AMNR')

    assert len(lista_noua) == len(lista) + 1
    assert new_object in lista_noua


def test_read():

    lista = get_data()
    random_object = lista[3]

    assert read(lista, get_id(random_object)) == random_object
    assert read(lista, None) == lista


def test_update():

    lista = get_data()
    new_object = get_new_object(5, 'minge', 'baschet', 25, 'AMNR')
    lista_noua = update(lista, new_object)

    assert len(lista) == len(lista_noua)
    assert new_object in lista_noua
    assert lista[1] == lista_noua[1]


def test_delete():

    lista = get_data()
    delete_id = 3
    delete_object = read(lista, delete_id)
    lista_noua = delete(lista, delete_id)

    assert len(lista_noua) == len(lista)-1
    assert delete_object not in lista_noua


def test_crud():

    test_create()
    test_read()
    test_update()
    test_delete()
