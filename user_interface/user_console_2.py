from Domain.object import get_new_object, get_object_string
from Logic.concatenare_string import concat_str
from Logic.crud import create, read, delete, update
from Logic.move_objects import move_objects


def handle_show_all(lista_obiecte):

    for obiect in lista_obiecte:
        print(get_object_string(obiect))


def handle_concatenare(lista_obiecte, lista_detalii_comanda):

    try:
        add_descriere = lista_detalii_comanda[1]
        pret = lista_detalii_comanda[2]

        lista_obiecte = concat_str(lista_obiecte, add_descriere, pret)
    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida", ve)

    return lista_obiecte


def handle_muta_obiectele(lista_obiecte, lista_detalii_comanda):

    initial_loc = lista_detalii_comanda[1]
    new_loc = lista_detalii_comanda[2]

    if len(initial_loc) != 4 or len(new_loc) != 4:
        raise ValueError("Numele locatiei trebuie sa fie de exact 4 caractere!")

    lista_obiecte = move_objects(lista_obiecte, initial_loc, new_loc)

    return lista_obiecte


def handle_modificare(lista_obiecte, lista_detalii_comanda):

    try:
        id = int(lista_detalii_comanda[1])
        nume = lista_detalii_comanda[2]
        descriere = lista_detalii_comanda[3]
        pret = lista_detalii_comanda[4]
        locatie = lista_detalii_comanda[5]

        new_object = get_new_object(id, nume, descriere, pret, locatie)
        lista_obiecte = update(lista_obiecte, new_object)

    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida, ve")

    return lista_obiecte


def handle_stergere(lista_obiecte, lista_detalii_comanda):

    try:
        id = int(lista_detalii_comanda[1])
        if read(lista_obiecte, id) is None:
            raise ValueError("Obiectul cu ID-ul introdus nu exista!")

        lista_obiecte = delete(lista_obiecte, id)

    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida pentru ID!", ve)

    return lista_obiecte


def handle_adaugare(lista_detalii_comanda, lista_obiecte):

    try:
        id = int(lista_detalii_comanda[1])
        nume = lista_detalii_comanda[2]
        descriere = lista_detalii_comanda[3]
        pret = lista_detalii_comanda[4]
        locatie = lista_detalii_comanda[5]
        return create(lista_obiecte, id, nume, descriere, pret, locatie)

    except ValueError as ve:
        print("Eroare, nu ati introdus o valoare valida", ve)

    return lista_obiecte


def show_menu():

    print(
        """
        Adaugare obiect :id_obiect,nume, descriere, pret achizitie, locatie
        Stergere obiect : id_obiect
        Modificare obiect id_obiect,nume, descriere, pret achizitie, locatie
        Muta toate obiectele dintr-o locatie in alta: locatie initiala, locatie finala
        Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare : descriere, pret" 
        Show all
        Iesire
        """
    )


def console_2():

    lista_obiecte = []

    done = False
    try:
        while not done:

            show_menu()
            comenzi = input("Introduceti comenzile separate prin ';', iar detaliitle pentru fiecare comanda prin ',': ")
            comenzi =comenzi.split(sep=";")

            for comanda in comenzi:

                comanda = comanda.split(sep=",")
                lista_detalii_comanda = []

                for detalii_comanda in comanda:

                    lista_detalii_comanda.append(detalii_comanda)

                if lista_detalii_comanda[0] == "Adaugare obiect":

                    lista_obiecte = handle_adaugare(lista_detalii_comanda, lista_obiecte)

                elif lista_detalii_comanda[0] == "Stergere obiect":

                    handle_stergere(lista_obiecte, lista_detalii_comanda)

                elif lista_detalii_comanda[0] == "Modificare obiect":

                    handle_modificare(lista_obiecte, lista_detalii_comanda)

                elif lista_detalii_comanda[0] == "Muta toate obiectele dintr-o locatie in alta":

                    handle_muta_obiectele(lista_obiecte, lista_detalii_comanda)

                elif lista_detalii_comanda[0] == "Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare":
                    # imi pare rau ca nu am gasit o denumire mai scurta

                    handle_concatenare(lista_obiecte, lista_detalii_comanda)

                elif lista_detalii_comanda[0] == "Show all":

                    handle_show_all(lista_obiecte)

                elif lista_detalii_comanda[0] == "Iesire":
                    done = True
                else:
                    print("Nu ati introdus o comanda valida!"
                          "Reincarcati.")
    except Exception as ex:
        print("Eroare, incercati din nou", ex)

