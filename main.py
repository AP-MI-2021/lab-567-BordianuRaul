from Tests.tests import test_crud, test_move_objects, test_concat_str, test_biggest_price_for_every_location
from user_interface.user_console import console


def main():

    console()


if __name__ == '__main__':
    test_biggest_price_for_every_location()
    test_concat_str()
    test_move_objects()
    test_crud()
    main()
