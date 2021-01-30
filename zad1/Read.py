'''
Napisz program który wczyta plik "input.txt" i na jego podstawie wygeneruje plik wyjściowy "output.txt".
Plik "input.txt" zawiera zapisane binarnie informacje o obiektach reprezentowanych przez 8 kolejnych bitów, składających się z 3 pól:
- 4 pierwsze bity reprezentują numer identyfikacyjny obiektu zapisany binarnie
- 3 kolejne bity reprezentują wiadomość
- 1 ostatni bit jest bitem kontrolnym - jeśli numer obiektu jest parzysty, to ten bit będzie miał wartość 0, w przeciwnym przypadku będzie równy 1

W pliku wyjściowym mają się znaleźć informacje:
- w pierwszej linii liczba wszystkich wczytanych obiektów
- w drugiej linii ilość obiektów zawierających błędy
- w trzeciej linii wszystkie obiekty które nie zawierały błędów, zapisane w formie i kolejności, w jakiej wystąpiły w pliku "input.txt"

Obiekt zawiera błędy, jeśli:
- wiadomość składa się wyłącznie z bitów równych 0
- bit kontrolny ma błędną wartość
'''

from Object import Object
import Write


def get_line(f):
    """Reads one byte from the given textfile"""
    c = f.read(8)
    while c:
        yield c
        c = f.read(8)


def read_file(file_name):
    """Reads textfile"""
    objects = [] # lista obiektów wczytanych z pliku
    with open("input.txt", encoding="utf-8") as f:

        for c in get_line(f):
            identification_number = c[0:4]
            message = c[4:7]
            control_bit = c[7:8]

            new_object = Object(identification_number, message, control_bit)
            objects.append(new_object)
            # print(c, sep=" ", end="\n")
    return objects
