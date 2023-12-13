list_1 = []
list_2 = []
list_3 = []
list_4 = []


def number_only(number):
    for e in number:
        if e != "0" and e != "1" and e != "2" and e != "3" and e != "4" and e != "5" and e != "6" and e != "7" and e != "8" and e != "9":
            return False
        else:
            acceptable = True
    return acceptable


def phone_numbers():
    list_4.clear()
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
                    print(
                        "You have already introduced this number, try again with a different number")
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


phone_numbers()
