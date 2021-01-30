"""
Napisz program konsolowy, który zależnie od wybranego trybu działania aplikacji:
- w jednym przypadku będzie konwertował liczby dziesiętne na binarne
- w drugim przypadku będzie konwertował liczby binarne na dziesiętne
i będzie wypisywał wyniki konwersji na ekranie.
"""
import sys
from numers import Bin_Number, Decimal_Number

class error_liczba_ujemna(Exception):
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def __str__(self):
        return 'self.wartosc'

class error_change_program(Exception):
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def str(self):
        return 'self.wartosc'


def do_program():
    version = present_menu()

    while version
    number = get_numer(version)

    if number is not None:
        print("Liczba {l} w systemie binarnym to {b}".format(l=number.dec_number(), b=number.bin_number()))

    # dec_to_bin()
    # bin_to_dec()

def present_menu():
    print("------------------------------------------------------------------------")
    print("Wybierz tryb działania aplikacji:")
    print("Kliknij 'd' aby wykonać konwersję liczby dziesiętnej na binarną")
    print("Kliknij 'b' aby wykonać konwersję liczby binarnej na dziesiętną")
    print("Kliknij 'e' aby wzakończyć działanie programu")
    print("------------------------------------------------------------------------\n")

    version = input("Tryb: ")

    return version

def get_numer(version):

    if version is 'd':
        print("------------------------------------------------------------------------")
        print("Wybrałeś opcję '1' - konwersja liczby dziesiętnej na binarną.")
        print("Naciśnij 'b' aby zmienić konwersję z liczby binarnej na dziesiętną")
        print("Naciśnij 'e' aby wzakończyć działanie programu")
        print("------------------------------------------------------------------------\n")

        liczba = input("Wpisz liczbę w systemie dziesiętnym: ")
        if liczba == 'd' or liczba == 'b' or liczba == 'e':
            return liczba
        else:
            return Decimal_Number(liczba)


    elif version is 'b':
        print("------------------------------------------------------------------------")
        print("Wybrałeś opcję '2' - konwersja liczby binarnej na dziesiętną")
        print("Naciśnij 'b' aby zmienić konwersję z liczby dziesiętnej na binarną")
        print("Naciśnij 'e' aby wzakończyć działanie programu")
        print("------------------------------------------------------------------------\n")

        liczba = input("Wpisz liczbę w systemie binarnym: ")

        if liczba == 'd' or liczba == 'b' or liczba == 'e':
            return liczba
        else:
            return Bin_Number(liczba)

    elif version is 'e':
        sys.exit(0)
    else:
        print("Wybrana opcja jest niedostępna.\n")
        return version





def dec_to_bin(liczba):
    try:
        if liczba == 'd' or liczba == 'b' or liczba == 'e':  raise error_change_program(liczba)
        liczba = int(liczba)
        if liczba <0: raise error_liczba_ujemna(liczba)
        liczba_bin = bin(liczba)[2:]
        print("Liczba {l} w systemie binarnym to {b}".format(l=liczba, b=liczba_bin))
    except error_change_program:
        check_version(str(liczba))
    except ValueError:
        print("To nie jest poprawna liczba.")
    except error_liczba_ujemna:
        print("Liczba nie może być ujemna. Aby zamienić liczbę ujemną należy użyć systemu U2.")

def bin_to_dec(liczba):
    try:
        if liczba == 'd' or liczba == 'b' or liczba == 'e':  raise error_change_program(liczba)
        liczba_bin = liczba
        liczba = int(liczba, 2)
        print("Liczba {b} w systemie dziesiętnym to {l}".format(l=liczba, b=liczba_bin))
    except error_change_program:
        check_version(str(liczba))
    except ValueError:
        print("To nie jest poprawna liczba.")

