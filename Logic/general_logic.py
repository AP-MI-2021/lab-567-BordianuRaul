from Domain.object2 import get_new_object
from Logic.crud import create


def citire(lista_obiecte):
    """
    Citire lista obiecte
    :param lista_obiecte:
    :return: lista de obiecte
    """

    _id = int(input("Introduceti ID-ul obiectului: "))
    _nume = input("Introduceti numele obiectului: ")
    _descriere = input("Introduceti o descriere pentru obiect: ")
    _pret_achizitie = int(input("Introduceti pretul de achizitie al obiectului: "))
    _locatie = input("Introduceti locatia obiectului: ")

    lista_obiecte = create(lista_obiecte, _id, _nume, _descriere, _pret_achizitie, _locatie)

    return lista_obiecte


def citire_new_object(id):
    """
    Citire a unui obiect nou
    :param id: id-ul obiectului nou
    :return: obiectul nou
    """

    _nume = input("Introduceti numele obiectului: ")
    _descriere = input("Introduceti o descriere pentru obiect: ")
    _pret_achizitie = int(input("Introduceti pretul de achizitie al obiectului: "))
    _locatie = input("Introduceti locatia obiectului: ")

    return get_new_object(id, _nume, _descriere, _pret_achizitie, _locatie)
