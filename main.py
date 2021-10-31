from Tests.tests import test_crud, test_move_objects
from user_interface.user_console import console


def main():

    console()


if __name__ == '__main__':
    test_move_objects()
    test_crud()
    main()
