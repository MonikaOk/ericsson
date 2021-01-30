'''
- 4 pierwsze bity reprezentują numer identyfikacyjny obiektu zapisany binarnie
- 3 kolejne bity reprezentują wiadomość
- 1 ostatni bit jest bitem kontrolnym - jeśli numer obiektu jest parzysty, to ten bit będzie miał wartość 0, w przeciwnym przypadku będzie równy 1

'''


class Object:
    def __init__(self, identification_number, message, control_bit):
        self.identification_number = identification_number
        self.message = message
        self.control_bit = control_bit

    def check_control_bit(self):
        # błąd gdy bit kontrolny ma błędną wartość
        # błąd zwraca (FALSE) gdy bit parzysty i bit kontrolny są równe
        even_number = int(self.identification_number) % 2
        bit_true = int(self.control_bit)

        if even_number == bit_true:
            return False
        else:
            return True

    def check_message(self):
        # błąd gdy wiadomość składa się wyłącznie z bitów równych 0
        if int(self.message) == 0:
            return True
        else:
            return False

    def check_error(self):
        if self.check_control_bit() or self.check_message():
            return True
        else:
            return False

    @property
    def object_write(self):
        return f"{self.identification_number}{self.message}{self.control_bit}".format(self=self)

    @property
    def decimal_identification_number(self):
        return f"{int(self.identification_number, 2)}".format(self=self)


