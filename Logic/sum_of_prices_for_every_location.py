from Domain.object import get_locatie, get_pret_achizitie


def create_location_price(location, price):
    """
    Creeaza un dictionar care contine locatia si suma preturilor locatiei
    :param location: locatia
    :param price: suma preturilor pentru locatie
    :return: un dictionar care contine locatia si suma preturilor pentru locatie
    """

    location_price = {
        'locatie': location,
        'pret_achizitie': price
    }

    return location_price


def get_sum(lista_obiecte, locatie):
    """
    Determina suma preturilor pentru o locatie din inventar
    :param locatie: locatia pentru care se doreste suma preturilor
    :param lista_obiecte: obiectele din inventar
    :return: suma preturilor
    """

    suma = 0

    for obiect in lista_obiecte:

        if get_locatie(obiect) == locatie:

            suma += get_pret_achizitie(obiect)

    return suma


def prices_sum_for_every_location(lista_obiecte):
    """
    Determina suma preturilor pentru fiecare locatie
    :param lista_obiecte: obiectele din inventar
    :return: o lista care contine fiecare locatie si suma preturilor pentru fiecare dintre acestea
    """

    result_list = []

    for obiect in lista_obiecte:

        locatie = get_locatie(obiect)
        suma = get_sum(lista_obiecte, locatie)
        location_price = create_location_price(locatie, suma)

        if location_price not in result_list:

            result_list.append(location_price)

    return result_list
