from Domain.object import get_locatie, get_pret_achizitie


def get_biggest_price(lista_obiecte, locatie):
    """
    Determina cel mai mare pret pentru o locatie
    :param lista_obiecte: lista de obiecte din inventar
    :param locatie:o locatie din inventar
    :return:
    """

    pret_maxim = 0

    for obiect in lista_obiecte:

        if get_locatie(obiect) == locatie:

            if pret_maxim < get_pret_achizitie(obiect):

                pret_maxim = get_pret_achizitie(obiect)

    return pret_maxim


def create_new_entity(locatie, pret_achizitie):
    """
    Creeaza un dictionar pentru o entitate care este alcatuita din locatie si pret
    :param locatie: locatia obiectului
    :param pret_achizitie: pretul obiectului
    :return:
    """

    locatie_pret = {
        'locatie': locatie,
        'pret_achizitie': pret_achizitie
    }

    return locatie_pret


def biggest_price_for_every_location(lista_obiecte):
    """
    Determina cel mai mare pret pentru fiecare locatie din inventar
    :param lista_obiecte: lista care contine toate obiectele din inventar
    :return: o lista care contine cel mai mare pret pentru fiecare locatie, respectiv locatiile acestor preturi
    """

    biggest_prices_list = []

    for obiect in lista_obiecte:

        locatie = get_locatie(obiect)
        pret_maxim = get_biggest_price(lista_obiecte, locatie)

        entity = create_new_entity(locatie, pret_maxim)

        if entity not in biggest_prices_list:
            biggest_prices_list.append(entity)

    return biggest_prices_list

