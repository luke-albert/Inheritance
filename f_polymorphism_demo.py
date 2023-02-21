# This program demonstrates polymorphism.

import f_animals as animals


def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    show_mammal_info(dog)
    show_mammal_info(cat)
    # show_mammal_info('Zerbra') #wont work because Zebra is a string and there is no show string method for a string object


'''
    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()
'''


def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print(f"{creature} is not from the normal class")


# Call the main function.
main()
