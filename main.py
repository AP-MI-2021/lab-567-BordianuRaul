from Tests.tests import test_crud, test_move_objects, test_concat_str
from user_interface.user_console import console


def main():

    console()


if __name__ == '__main__':
    test_concat_str()
    test_move_objects()
    test_crud()
    main()
