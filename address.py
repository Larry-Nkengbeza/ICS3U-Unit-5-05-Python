# This program was created by Larry Nkengbeza
# This program was created in January 2020
# This program gives users adresses


def address(adressee, st_number, st_name, city, pe, pc, apt=None):

    address = adressee
    address = address + " " + st_number
    address = address + " " + st_name
    if apt != None:
        address = address + " " + apt
    address = address + " " + city
    address = address + " " + pe
    address = address + " " + pc

    return address


def main():

    apartment = None

    adressee = input("Enter the adressee: ")
    st_number = input("Enter your street number: ")
    st_name = input("Enter your street name: ")
    question = input("Do you live in an apartment? Y/N: ")
    if question == "Y" or question == "Yes":
        apt = input("Enter your aparment number: ")
    city = input("Enter the city you live in: ")
    pe = input("Enter the province you live in: ")
    pc = input("Enter the your postal_code: ")

    if apartment != None:
        full_address = address(adressee, st_number, st_name, city, pe, pc, apt)
    else:
        full_address = address(adressee, st_number, st_name, city, pe, pc)

    print(full_address)


if __name__ == "__main__":
    main()
