from abc import ABC, abstractmethod

class error_change_program(Exception):
    def __init__(self, wartosc):
        self.wartosc = wartosc
    def str(self):
        return 'self.wartosc'

class Number(ABC):
    def __init__(self, number):
        self.__number = number

    @abstractmethod
    def dec_number(self):
        pass

    @abstractmethod
    def bin_number(self):
        pass

class Bin_Number(Number):
    def __init__(self, bin_number):
        self.__number = bin_number

    def dec_number(self):
        return int(self.__number, 2)

    def bin_number(self):
        return self.__number


class Decimal_Number(Number):
    def __init__(self, dec_number):
        self.__number = dec_number

    def dec_number(self):
        try:
            if self.__number == 'd' or self.__number == 'b' or self.__number == 'e':  return None
            dec_number = int(self.__number)
            if dec_number < 0: return None
        except ValueError:
            return None
        except TypeError:
            return None

        return dec_number

    def bin_number(self):

        try:
            if self.__number == 'd' or self.__number == 'b' or self.__number == 'e':  return None
            bin_number = bin(self.dec_number())[2:]
        except ValueError:
            return None
        except TypeError:
            return None

        return bin_number

