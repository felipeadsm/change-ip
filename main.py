from inteface import Interface

import pyuac


def main():
    Interface()


if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        main()
