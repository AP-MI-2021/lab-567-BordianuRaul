from Domain.object import get_new_object, get_id
from Logic.biggest_price_for_every_location import biggest_price_for_every_location, create_new_entity
from Logic.concatenare_string import concat_str
from Logic.crud import create, read, update, delete
from Logic.move_objects import move_objects
from Logic.order_objects_ascending_by_price import order_objects
from Logic.sum_of_prices_for_every_location import create_location_price, prices_sum_for_every_location
from user_interface.user_console import handle_new_list, handle_undo, handle_redo


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


def test_move_objects():

    lista_obiecte = get_data()

    assert move_objects(lista_obiecte, 'DEPO', 'DEP7') == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEP7'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEP7'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'IKEA')
    ]

    lista_obiecte = get_data()

    assert move_objects(lista_obiecte, 'IKEA', 'DEP7') == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar', 2350, 'DEP7'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'DEP7')
    ]

    lista_obiecte = get_data()

    assert move_objects(lista_obiecte, 'AMnR', 'DEP7') == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'DEP7'),
        get_new_object(3, 'dulap', 'lemn de stejar', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'IKEA')
    ]


def test_concat_str():

    lista_obiecte = get_data()

    assert concat_str(lista_obiecte, ' de vanzare', 10) == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal de vanzare', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar de vanzare', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ de vanzare', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires de vanzare', 1500, 'IKEA')
    ]

    lista_obiecte = get_data()

    assert concat_str(lista_obiecte, ' va fi redus', 25) == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar va fi redus', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ va fi redus', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires va fi redus', 1500, 'IKEA')
    ]

    lista_obiecte = get_data()

    assert concat_str(lista_obiecte, " isi va pastra pretul", 1500) == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(3, 'dulap', 'lemn de stejar isi va pastra pretul', 2350, 'IKEA'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'IKEA')
    ]


def test_biggest_price_for_every_location():

    lista_obiecte = get_data()

    assert biggest_price_for_every_location(lista_obiecte) == [
        create_new_entity('DEPO', 50),
        create_new_entity('AMnR', 25),
        create_new_entity('IKEA', 2350)
    ]


def test_order_objects():

    lista_obiecte = get_data()

    assert order_objects(lista_obiecte) == [
        get_new_object(1, 'cactus', 'decorativ', 10, 'DEPO'),
        get_new_object(2, 'minge', 'fotbal', 25, 'AMnR'),
        get_new_object(4, 'orhidee', 'decorativ', 50, 'DEPO'),
        get_new_object(5, 'masa', 'lemn de cires', 1500, 'IKEA'),
        get_new_object(3, 'dulap', 'lemn de stejar', 2350, 'IKEA')

    ]


def test_prices_sum_for_every_location():

    lista_obiecte = get_data()

    assert prices_sum_for_every_location(lista_obiecte) == [
        create_location_price('DEPO', 60),
        create_location_price('AMnR', 25),
        create_location_price('IKEA', 3850)
    ]


def test_undo_redo():

    # 1
    lista_obiecte = []
    curent_version = 0
    versions_list = [lista_obiecte]

    # 2
    lista_obiecte = create(lista_obiecte, 1, 'cactus', 'decorativ', 10, 'DEPO')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    # 3
    lista_obiecte = create(lista_obiecte, 2, 'minge', 'fotbal', 25, 'AMnR')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    # 4
    lista_obiecte = create(lista_obiecte, 3, 'dulap', 'lemn de stejar', 2350, 'IKEA')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    # 5
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 2

    # 6
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 1

    # 7
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 0

    # 8

    assert handle_undo(versions_list, curent_version) is None

    # 9
    lista_obiecte = create(lista_obiecte, 1, 'cactus', 'decorativ', 10, 'DEPO')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    lista_obiecte = create(lista_obiecte, 2, 'minge', 'fotbal', 25, 'AMnR')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    lista_obiecte = create(lista_obiecte, 3, 'dulap', 'lemn de stejar', 2350, 'IKEA')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    # 10
    assert handle_redo(versions_list, curent_version) is None

    # 11
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 2

    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 1

    # 12
    lista_obiecte, curent_version = handle_redo(versions_list, curent_version)

    assert len(lista_obiecte) == 2

    # 13
    lista_obiecte, curent_version = handle_redo(versions_list, curent_version)

    assert len(lista_obiecte) == 3

    # 14
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 2

    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 1

    # 15

    lista_obiecte = create(lista_obiecte, 4, 'orhidee', 'decorativ', 50, 'DEPO')
    versions_list, curent_version = handle_new_list(versions_list, curent_version, lista_obiecte)

    assert len(lista_obiecte) == 2

    # 16
    assert handle_redo(versions_list, curent_version) is None

    # 17
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 1

    # 18
    lista_obiecte, curent_version = handle_undo(versions_list, curent_version)

    assert len(lista_obiecte) == 0

    # 19
    lista_obiecte, curent_version = handle_redo(versions_list, curent_version)

    assert len(lista_obiecte) == 1

    lista_obiecte, curent_version = handle_redo(versions_list, curent_version)

    assert len(lista_obiecte) == 2

    # 20

    assert handle_redo(versions_list, curent_version) is None
