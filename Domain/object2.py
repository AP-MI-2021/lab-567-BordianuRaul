

def get_new_object(_id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):

    lista_obiect = [_id, _nume, _descriere, _pret_achizitie, _locatie]

    return lista_obiect


def get_id(lista_obiect):
    return lista_obiect[0]


def get_nume(lista_obiect):
    return lista_obiect[1]


def get_descriere(lista_obiect):
    return lista_obiect[2]


def get_pret_achizitie(lista_obiect):
    return lista_obiect[3]


def get_locatie(lista_obiect):
    return lista_obiect[4]
