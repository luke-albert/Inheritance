class Person:

    def __init__(self, name, address, tel_number):
        self.__name = name
        self.__address = address
        self.__telnumber = tel_number

    def print_person(self, name, address, tel_number):
        print('Name', name)
        print('Address', address)
        print('Telephone Number:', tel_number)


class Customer(Person):

    def __init__(self, name, address, tel_number, cust_number, boolean_data):

        Person.__init__(self, name, address, tel_number):

        self.__custnumber = cust_number
        self.__boolean = boolean_data
