from Domain.object import get_pret_achizitie, get_descriere, get_id, get_nume, get_new_object, get_locatie


def concat_str(lista_obiecte, add_descriere, pret):
    """

    :param lista_obiecte: lista de obiecte din inventar
    :param add_descriere:un string care va fi concatenat la finalul tutoror descrierilor obiectelor /
                               cu pretul de achizitie mai mare decat 'pret'
    :param pret:un pret
    :return:lista de obiecte cu descrierile modificate
    """

    result = []

    for obiect in lista_obiecte:

        if get_pret_achizitie(obiect) > pret:

            result.append(get_new_object(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect) + add_descriere,
                get_pret_achizitie(obiect),
                get_locatie(obiect)
            )
            )
        else:
            result.append(obiect)

    return result
