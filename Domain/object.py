

def get_new_object(_id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):
    """
    Creeaza un obiect
    :param _id:
    :param _nume:
    :param _descriere:
    :param _pret_achizitie:
    :param _locatie:
    :return: obiectul
    """
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret_achizitie': _pret_achizitie,
        'locatie': _locatie


    }

    return obiect


def get_id(obiect):
    return obiect['id']


def get_nume(obiect):
    return obiect['nume']


def get_descriere(obiect):
    return obiect['descriere']


def get_pret_achizitie(obiect):
    return obiect['pret_achizitie']


def get_locatie(obiect):
    return obiect['locatie']
