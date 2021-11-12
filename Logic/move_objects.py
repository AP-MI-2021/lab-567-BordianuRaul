from Domain.object import get_locatie, get_new_object, get_pret_achizitie, get_descriere, get_nume, get_id


def is_part_of(lista_obiecte, initial_loc):

    for obiect in lista_obiecte:
        if obiect['locatie'] == initial_loc:
            return True
    else:
        return False


def move_objects(lista_obiecte, initial_loc, new_loc):
    """
    Muta toate obiectele dintr-o locatie in alta

    :param lista_obiecte: obiectele din inventarul institutiei
    :param initial_loc:locatia initiala a obiectului
    :param new_loc:locatia noua, in care va fi mutat obiectul
    :return:lista cu obiectele din inventarul institutiei, actualizata
    """

    result = []

    if is_part_of(lista_obiecte, initial_loc) is False:
        raise ValueError("Locatia introdusa nu exista!")

    for obiect in lista_obiecte:
        if get_locatie(obiect) == initial_loc:

            result.append(get_new_object(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret_achizitie(obiect),
                new_loc
            )
            )

        else:
            result.append(obiect)

    return result
