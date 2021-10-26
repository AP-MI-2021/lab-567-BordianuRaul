from Logic.crud import delete, update
from Logic.general_logic import citire, citire_new_object


def show_menu():

    print("""
        1.Adaugare obiect
        2.Stergere obiect
        3.Modificare obiect
        4.Show all
        x.Iesire program
    """)


def console():

    lista_obiecte = []

    while True:

        show_menu()

        optiune = input("Selectati optiunea: ")

        if optiune == '1':

            lista_obiecte = citire(lista_obiecte)

        elif optiune == '2':

            id_obiect = int(input("Introduceti ID-ul obiectului pe care doriti sa il stergeti: "))
            lista_obiecte = delete(lista_obiecte, id_obiect)

        elif optiune == '3':

            id_obiect = int(input("Introduceti ID-ul obiectului pe care doriti sa il modificati: "))
            new_object = citire_new_object(id_obiect)
            lista_obiecte = update(lista_obiecte, new_object)

        elif optiune == '4':

            print(lista_obiecte)

        elif optiune == 'x':
            break

        else:
            print("Optiune invalida!")
