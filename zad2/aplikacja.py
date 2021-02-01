import Class_number
import sys
def start_program():
    '''
    Program jest wykonywany w pętli. pozwala na kilkuktorną zmaine wartosci, ale trzeba za kazdym razem wybrac typ programu
    '''
    # wybranie opcji działania programu

    while True:
        version = present_menu()
        program = choce_program_version(version)

        # Wpisanie nowej liczby
        if program != '0':
            num = Class_number.Number(program)
            num.add_number()
            num.print_number()

def present_menu():
    print("------------------------------------------------------------------------")
    print("Wybierz tryb działania aplikacji:")
    print("Kliknij 'd' aby wykonać konwersję liczby dziesiętnej na binarną")
    print("Kliknij 'b' aby wykonać konwersję liczby binarnej na dziesiętną")
    print("Kliknij 'e' aby wzakończyć działanie programu")
    print("------------------------------------------------------------------------\n")

    version = input("Tryb: ")

    return version

def choce_program_version(version):

    program = None

    if version is 'd':
        print("------------------------------------------------------------------------")
        print("Wybrałeś opcję '1' - konwersja liczby dziesiętnej na binarną.")
        print("------------------------------------------------------------------------\n")
        program = '1'

    elif version is 'b':
        print("------------------------------------------------------------------------")
        print("Wybrałeś opcję '2' - konwersja liczby binarnej na dziesiętną")
        print("------------------------------------------------------------------------\n")
        program = '2'

    elif version is 'e':
        sys.exit(0)
    else:
        print("Wybrana opcja jest niedostępna. Wybierz ponownie.\n")
        program = '0'
    return program