from Domain.object import get_pret_achizitie


def order_objects(lista_obiecte):
    """
    Ordoneaza crescator obiectele din inventar dupa pretul de achizitie
    :param lista_obiecte: lista care contine obiectele din inventar
    :return: lista sortata
    """

    result = sorted(lista_obiecte, key=get_pret_achizitie)

    return result
