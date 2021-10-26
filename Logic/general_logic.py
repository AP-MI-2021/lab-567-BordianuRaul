from Logic.crud import create


def citire(lista_obiecte):

        _id = int(input("Introduceti ID-ul obiectului: "))
        _nume = input("Introduceti numele obiectului: ")
        _descriere = input("Introduceti o descriere pentru obiect: ")
        _pret_achizitie = int(input("Introduceti pretul de achizitie al obiectului: "))
        _locatie = input("Introduceti locatia obiectului: ")

        lista_obiecte = create(lista_obiecte, _id, _nume, _descriere, _pret_achizitie, _locatie)

        return lista_obiecte
