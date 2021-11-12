from Tests.tests import test_crud, test_move_objects, test_concat_str, test_biggest_price_for_every_location, \
    test_order_objects, test_prices_sum_for_every_location, test_undo_redo
from user_interface.user_console import console


def main():

    lista = []
    console(lista)


if __name__ == '__main__':

    test_undo_redo()
    test_prices_sum_for_every_location()
    test_order_objects()
    test_biggest_price_for_every_location()
    test_concat_str()
    test_move_objects()
    test_crud()
    main()
