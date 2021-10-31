from Domain.object import get_locatie


def is_part_of(lista_obiecte, initial_loc):

    for obiect in lista_obiecte:
        if obiect['locatie'] == initial_loc:
            return True
    else:
        return False


def move_objects(lista_obiecte, initial_loc, new_loc):
    """

    :param lista_obiecte: obiectele din inventarul institutiei
    :param initial_loc:locatia initiala a obiectului
    :param new_loc:locatia noua, in care va fi mutat obiectul
    :return:lista cu obiectele din inventarul institutiei, actualizata
    """

    if is_part_of(lista_obiecte, initial_loc) is False:
        raise ValueError("Locatia introdusa nu exista!")

    for obiect in lista_obiecte:
        if get_locatie(obiect) == initial_loc:
            obiect['locatie'] = new_loc

    return lista_obiecte
