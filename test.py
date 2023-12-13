idp = []  # this variable is for
namep = []
surnamep = []
adressp = []
numberp = []
cityp = []
list_1 = []
list_2 = []
list_3 = []


def number_in_string(string):
    numbers = "0123456789"
    for e in numbers:
        for y in string:
            if e == y:
                print("Yoy only can enter a letter")
                return False
            else:
                acceptable = True
    return acceptable


def customer_management():

    print("***************************************************************")
    print("*                    Customer Management Menu                 *")
    print("***************************************************************")
    print("1. New Customer")
    print("2. Print Customers")
    print("3. Search Customer by ID")
    print("4. Search Customer by telephone number")
    print("B. Back")
    print("E. End")
    option = input("Please, insert a valid option (1-3, E or B): ")

    if option == "1":
        print("You have selected option 1")
        new_customer()
    elif option == "2":
        print("You have selected option 2")
    elif option == "3":  # Search customer by ID
        if len(idp) == 0:  # There are no customers registered
            print(
                "There are no customers registered yet. Do you want to be our first customer?")
        else:
            abc = 1
            while abc != 0:
                x = 1
                d = 0
                t = 0
                while x != 0:  # Validates that the entered ID is valid
                    custmor = input("Please, customer ID? ")
                    if custmor[-1] == "A":
                        x = x-1
                        z = 0
                    else:
                        print("The field has to finish with the letter A")
                        z = 1
                while z != 1:
                    if d < len(idp):
                        if idp[d] == custmor:
                            z = 1
                            print("ID:", idp[d])
                            print("Name:", namep[d])
                            print("Surname:", surnamep[d])
                            print("Adress:", adressp[d])
                            print("Number:", numberp[d])
                            print("City:", cityp[d])
                            print("Phone number:", list_3[d])

                            abc = 0
                        else:
                            d = d+1
                    else:
                        while t == 0:
                            print(
                                "Error that customer does not exist. Do you want to try again?")
                            print("1. Try again")
                            print("2. Back to customer management menu")
                            n = input("Please insert a valid option 1 or 2: ")
                            if n == "1":
                                t = 1
                                z = 1
                            elif n == "2":
                                abc = 0
                                t = 1
                                z = 1
                            else:
                                print("Error, invalid option")
        customer_management()
    elif option == "4":
        if len(list_3) == 0:
            print(
                "There are no customers registered yet. Do you want to be our first customer?")
        else:
            telephone = input("Please, customer phone number? ")
            match = False
            p = 0
            for i in list_3:
                p += 1
                for n in i:
                    for e in n:
                        if e == telephone:
                            print("ID:", idp[p])
                            print("Name:", namep[p])
                            print("Surname:", surnamep[p])
                            print("Adress:", adressp[p])
                            print("Number:", numberp[p])
                            print("City:", cityp[p])
                            print("Phone number:", list_3[p])
                            match = True
            if match == False:
                print("Error, that customer does not exists")

    elif option == "E" or option == "e":
        print("You have selected to exit from the customer management menu")
    elif option == "B" or option == "b":
        main_menu()
    else:
        print("Error: invalid option in customer management menu ")
        customer_management()


def new_customer():
    d = 0
    x = 1
    while x != 0:
        z = 0
        ID = input("Please introduce your ID: ")
        if ID[-1] == "A":
            x = x-1
        else:
            print("The field has to finish with the letter A")
        if x == 0:
            while z != 1:
                if d < len(idp):
                    if idp[d] == ID:
                        print(
                            "Error that customer already exists. Please insert another ID")
                        z = 1
                        x = 1
                    else:
                        d = d+1
                else:
                    z = 1
    idp.append(ID)
    valid = False
    while valid == False:
        name = input("Introduce your name:")
        valid = number_in_string(name)

    namep.append(name)
    valid = False
    while valid == False:
        surname = input("Introduce your surname:")
        valid = number_in_string(surname)
    surnamep.append(surname)
    x = 1
    while x != 0:
        adress = input("Please introduce your adress: ")
        if len(adress) < 3:
            print("The field must be 3 or more characters")
        else:
            x = x-1
    adressp.append(adress)
    valid = False
    '''while valid == False:
        number = input("Introduce your phone:")
        valid = number_only(number)

    numberp.append(number)'''
    x = 1
    while x != 0:
        city = input("Please introduce your city name: ")
        if len(city) < 3:
            print("The field must be 3 or more characters")
        else:
            x = x-1
    cityp.append(city)
    phone_numbers()

    print("SUCCESS - the data of the new customer is:")
    print("Name:     ", name)
    print("Surname:  ", surname)
    print("ID:       ", ID)
    print("Adress:   ", adress)
    print("City:     ", city)
    print("Phone:    ", list_2)

    customer_management()


def number_only(number):
    for e in number:
        if e != "0" and e != "1" and e != "2" and e != "3" and e != "4" and e != "5" and e != "6" and e != "7" and e != "8" and e != "9":
            return False
        else:
            acceptable = True
    return acceptable


def phone_numbers():
    counter = 0
    list_2 = []
    valid = False
    while valid == False:
        ty = input("How many phone numbers do you want to introduce?: ")
        valid = number_only(ty)

    while counter < int(ty):
        list_1 = []
        # To validadte that there are only numbers
        valid = False
        while valid == False or len(phone) != 9:
            phone = input("Introduce a valid phone number: ")
            valid = number_only(phone)

        if len(list_2) >= 1:  # The list_2 storages the phone numbers ()
            q = 0
            while q < len(list_2):  # Validates that the phone numbers are different
                if phone == list_2[q][0]:
                    q = q+len(list_2)
                    phone = input(
                        "You have already introduced this number, try again with a different number: ")
                else:
                    q = q+1

        name_phone = input(
            "Please introduce the description of the phone number: ")
        list_1.append(phone)
        # The list_1 list is storaging the phone numbers with its respective name
        list_1.append(name_phone)
        counter += 1
        t = 0
        q = 0
        while t == 0:
            if len(list_2) >= 1:
                if q < len(list_2):  # (The list_2 is not empty)
                    # (To order the telephone number)
                    if list_1[0] > list_2[q][0]:
                        q = q+1
                    else:
                        list_2.insert(q, list_1)
                        t = 1
                else:
                    list_2.append(list_1)
                    t = 1
            else:
                list_2.append(list_1)
                t = 1
    list_3.append(list_2)


def management_menus(section):
    print("***************************************************************")
    print("*                  " + section +
          " Management Menu                    *")
    print("***************************************************************")
    print("1. New", section)
    print("2. Print", section)
    print("3. Search ", section, " by ID")
    print("B. Back")
    print("E. End")
    option = input("Please, insert a valid option (1-3, E or B): ")

    if option == "1":
        print("You have selected option 1")
    elif option == "2":
        print("You have selected option 2")
    elif option == "3":
        print("You have selected option 3")
    elif option == "E" or option == "e":
        print("You have selected to exit from the sensor management menu")
    elif option == "B" or option == "b":
        main_menu()
    else:
        print("Error: invalid option in sensor management menu ")


def main_menu():

    print("***************************************************************")
    print("*                          Main Menu                          *")
    print("***************************************************************")
    print("1. Customer Management")
    print("2. Sensor Management")
    print("3. Security System Management")
    print("4. Sales Management")
    print(" ")
    print("E. End")
    print("")

    option = input("Please, insert a valid option (1-4, E): ")

    if option == "1":
        customer_management()

    elif option == "2":
        management_menus("sensor")

    elif option == "3":
        management_menus("systems")

    elif option == "4":
        management_menus("sales")

    elif option == "E" or option == "e":
        print("You have selected to exit from the main menu")
    else:
        print("Error: invalid option in main menu ")
        main_menu()


main_menu()
