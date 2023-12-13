telephone = input("Please, customer phone number? ")
match = False
for i in list_3:
    for n in i:
        for e in n:
            if e == telephone:
                print("ID:", idp[e])
                print("Name:", namep[e])
                print("Surname:", surnamep[e])
                print("Adress:", adressp[e])
                print("Number:", numberp[e])
                print("City:", cityp[e])
                print("Phone number:", list_3[e])
                match = True
if match == False:
    print("Error, that customer does not exists")
