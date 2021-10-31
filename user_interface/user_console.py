from Domain.object import get_new_object, get_object_string
from Logic.concatenare_string import concat_str
from Logic.crud import delete, update, create, read
from Logic.move_objects import move_objects


def handle_create(lista_obiecte):

    try:
        id_obiect = int(input("Introduceti ID-ul obiectului: "))
        if read(lista_obiecte, id_obiect) is not None:
            raise ValueError("Exista deja un obiect cu acest ID!")
        nume = input("Introduceti numele obiectului: ")
        descriere = input("Introduceti descrierea obiectului: ")
        pret_achizitie = int(input("Introduceti pretul de achizitie al obiectlui: "))
        locatie = input("Introduceti locatia obiectului: ")
        return create(lista_obiecte, id_obiect, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida!", ve)

    return lista_obiecte


def handle_delete(lista_obiecte):

    try:
        id_obiect = int(input("Introduceti ID-ul elementului pe care doriti sa il stergeti: "))

        if read(lista_obiecte, id_obiect) is None:
            raise ValueError("Obiectul cu ID-ul introdus nu exista!")

        lista_obiecte = delete(lista_obiecte, id_obiect)

    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida pentru ID!", ve)

    return lista_obiecte


def handle_update(lista_obiecte):

    try:
        id_obiect = int(input("Introduceti ID-ul obiectului pe care doriti sa il modificati: "))
        if read(lista_obiecte, id_obiect) is None:
            raise ValueError("Obiectul cu ID-ul introdus nu exista!")
        nume = input("Introduceti numele obiectului: ")
        descriere = input("Introduceti descrierea obiectului: ")
        pret_achizitie = int(input("Introduceti pretul de achizitie al obiectlui: "))
        locatie = input("Introduceti locatia obiectului: ")

        new_object = get_new_object(id_obiect, nume, descriere, pret_achizitie, locatie)
        lista_obiecte = update(lista_obiecte, new_object)

    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida!", ve)

    return lista_obiecte


def handle_show_all(lista_obiecte):

    for obiect in lista_obiecte:
        print(get_object_string(obiect))


def handle_move_objects(lista_obiecte):

    initial_loc = input("Introduceti locatia din care doriti sa se mute obiectele: ")
    new_loc = input("Introduceti locatia unde doriti sa se mute obiectele: ")

    if len(initial_loc) != 4 or len(new_loc) != 4:
        raise ValueError("Numele locatiei trebuie sa fie de exact 4 caractere!")

    lista_obiecte = move_objects(lista_obiecte, initial_loc, new_loc)

    return lista_obiecte


def handle_concat_str(lista_obiecte):

    try:
        add_descriere = input("Introduceti mesajul pe care doriti sa il adaugati descrierilor: ")
        pret = int(input("Introduceti pretul: "))

        lista_obiecte = concat_str(lista_obiecte, add_descriere, pret)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida", ve)

    return lista_obiecte


def show_menu():

    print("""
        1.Adaugare obiect
        2.Stergere obiect
        3.Modificare obiect
        4.Muta toate obiectele dintr-o locatie in alta
        5.Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare.
        S.Show all
        x.Iesire program
    """)


def console():

    lista_obiecte = []

    while True:

        try:
            show_menu()

            optiune = input("Selectati optiunea: ")

            if optiune == '1':

                lista_obiecte = handle_create(lista_obiecte)

            elif optiune == '2':

                handle_delete(lista_obiecte)

            elif optiune == '3':

                handle_update(lista_obiecte)

            elif optiune == '4':

                handle_move_objects(lista_obiecte)

            elif optiune == '5':

                handle_concat_str(lista_obiecte)

            elif optiune == 'S':

                handle_show_all(lista_obiecte)

            elif optiune == 'x':
                break

            else:
                print("Optiune invalida!")

        except Exception as ex:
            print("Eroare", ex)
