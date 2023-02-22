class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Telephone Number:', self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, cust_number, on_list):
        Person.__init__(self, name, address, phone)
        self.__cust_number = cust_number
        self.__on_list = on_list

    def print_person(self):
        Person.print_person(self)

        print(f"Customer Number: {self.__cust_number}")
        if self.__on_list:  # checking to see if it has a value
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")
