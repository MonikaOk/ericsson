
class Number():

    def __init__(self, program):
        self.program = program
        self.bin_number = 0
        self.dec_number = 0


    def add_number(self):
        '''
        metoda do dodawania nowej liczby do klasy
        :return:
        '''
        if self.program == '1':
            number = input("Wpisz liczbę w systemie dziesiętnym: ")
            self.dec_number = self.make_from_dec_number(number)
        elif self.program == '2':
            number = input("Wpisz liczbę w systemie binarnym: ")
            self.dec_number = self.make_from_bin_number(number)
        else:
            number = None
        self.bin_number = bin(self.dec_number)[2:]

    def make_from_dec_number(self, number, returnNumber=None, wrongNumber=False):
        '''
        funkcja przekształca wspisaną liczna na dec
        :param number: liczba w str do zamiany
        :param returnNumber: zwracana liczba
        :param wrongNumber: blednie wpisana liczba
        :return: returnNumber : liczba zwraca w poprawnym formacie
        '''
        while True:

            try:
                int(number)
                wrongNumber = False
            except ValueError:
                wrongNumber = True

            #liczba musi być > 0, aby można zamienić ją na binarną
            if (wrongNumber == False)  and (int(number) > 0 ):
                returnNumber = int(number)
                break
            else:
                number = input("Wpisz liczbę w systemie dziesiętnym: ")

        return returnNumber

    def make_from_bin_number(self, number, returnNumber=None, wrongNumber=False):
        '''
        funkcja przekształca wspisaną liczbe na bin
        :param number: liczba w str do zamiany
        :param returnNumber: zwracana liczba
        :param wrongNumber: blednie wpisana liczba
        :return: returnNumber : liczba zwraca w poprawnym formacie
        '''
        while True:

            try:
                int(number,2)
                wrongNumber = False
            except ValueError:
                wrongNumber = True

            #liczba musi być > 0, aby można zamienić ją na binarną
            if (wrongNumber == False):
                returnNumber = int(number, 2)
                break
            else:
                number = input("Wpisz liczbę w systemie binarnym: ")

        return returnNumber

    def print_number(self):
        program = {}
        program['2'] = 'dziesiętnym'
        program['1'] = 'binarnym'
        print("Liczba {l} w systemie {s} to {b}".format(l=self.dec_number, b=self.bin_number, s=program[self.program]))


2