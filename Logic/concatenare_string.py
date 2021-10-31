from Domain.object import get_pret_achizitie


def concat_str(lista_obiecte, add_descriere, pret):
    """

    :param lista_obiecte: lista de obiecte din inventar
    :param add_descriere:un string care va fi concatenat la finalul tutoror descrierilor obiectelor /
                               cu pretul de achizitie mai mare decat 'pret'
    :param pret:un pret
    :return:lista de obiecte cu descrierile modificate
    """

    for obiect in lista_obiecte:

        if get_pret_achizitie(obiect) > pret:
            obiect['descriere'] = obiect['descriere'] + add_descriere

    return lista_obiecte
