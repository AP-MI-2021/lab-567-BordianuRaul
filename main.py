from Tests.tests import test_crud, test_move_objects, test_concat_str
from user_interface.user_console_2 import console_2


def main():

    console_2()


if __name__ == '__main__':
    test_concat_str()
    test_move_objects()
    test_crud()
    main()
