idp=[]
namep=[]
surnamep=[]
adressp=[]
numberp=[]
cityp=[]
list_3=[]
list_4=[]
def customer_management():

	print("***************************************************************")
	print("*                    Customer Management Menu                 *")
	print("***************************************************************")
	print("1. New Customer")
	print("2. Print Customers")
	print("3. Search Customer by ID")
	print("B. Back")
	print("E. End")
	option = input("Please, insert a valid option (1-3, E or B): ")

	if option == "1":
		print("You have selected option 1")
		new_customer()
	elif option == "2":
		print("You have selected option 2")
	elif option == "3":
		if len(idp)==0:
			print("There are no customers registered yet. Do you want to be our first customer?")
		else:
			abc=1
			while abc!=0:
				x = 1
				d=0
				t=0
				while x != 0:
					custmor=input("Please, customer ID? " )
					if custmor[-1] == "A":
						x = x-1
						z=0
					else:
						print("The field has to finish with the letter A")
						z=1
				while z!=1:
					if d<len(idp):
						if idp[d]==custmor:
							z=1
							print("ID:", idp[d])
							print("Name:", namep[d])
							print("Surname:", surnamep[d] )
							print("Adress:", adressp[d])
							print("Number:", numberp[d])
							print("City:", cityp[d])
							print("Phone number:", list_3[d])
							
							abc=0
						else:
							d=d+1
					else:
						while t==0:
							print("Error that customer does not exist. Do you want to try again?")
							print("1. Try again")
							print("2. Back to customer management menu")
							n=input("Please insert a valid option 1 or 2: ")
							if n=="1":
								t=1
								z=1
							elif n=="2":
								abc=0
								t=1
								z=1
							else:
								print("Error, invalid option")
		customer_management()

	elif option == "E" or option == "e":
		print("You have selected to exit from the customer management menu")
	elif option == "B" or option == "b":
		main_menu()
	else:
		print("Error: invalid option in customer management menu ")
		customer_management()
def new_customer():
	d=0
	x = 1
	while x != 0:
		z=0
		ID = input("Please introduce your ID: ")
		if ID[-1] == "A":
			x = x-1
		else:
			print("The field has to finish with the letter A")
		if x==0:
			while z!=1:
				if d<len(idp):
					if idp[d]==ID:
						print("Error that customer already exists. Please insert another ID")
						z=1
						x=1
					else:
						d=d+1
				else:
					z=1
	idp.append(ID)
	z = 0
	while z==0:
		x = 0
		y = 0
		name = input("Introduce your name: ")
		j=("0123456789")
		while x < len(name):
			if y < 10:
				if j[y] == name[x]:
					print("The field only accepts letters")
					x=x+len(name)
				else:
					y = y + 1
			else:
				x=x+1
				y=0
			if len(name)==x:
				z=1
	namep.append(name)
	z = 0
	while z==0:
		x = 0
		y = 0
		surname = input("Introduce your surname: ")
		j=("0123456789")
		while x < len(surname):
			if y < 10:
				if j[y] == surname[x]:
					print("The field only accepts letters")
					x=x+len(surname)
				else:
					y = y + 1
			else:
				x=x+1
				y=0
			if len(surname)==x:
				z=1
	surnamep.append(surname)
	x = 1
	while x != 0:
		adress = input("Please introduce your adress: ")
		if len(adress) < 3:
			print("The field must be 3 or more characters")
		else:
			x = x-1
	adressp.append(adress)
	x = 1
	while x != 0:
		number = int(input("Please introduce your number: "))
		if number < 0:
			print("The field must be positive")
		else:
			x = x-1
	numberp.append(number)
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
	print("Phone:    ", list_4)
	
	customer_management()
def phone_numbers():
	list_4.clear()
	o=0
	list_2=[]
	ty=int(input("How many phone numbers for user? " ))
	while o<ty:
		list_1=[]
		z = 0
		while z < 9:
			x = 0
			z = 0
			y = 0
			phone = input("Introduce your phone number: ")
			j =("0123456789")
			while x < 9:
				if len(phone) == 9:
					if y < 10:
						if j[y] == phone[x]:
							x = x + 1
							z = z + 1
							y = 0
						else:
							y = y + 1
					else:
						print("The field only accepts numbers")
						x = x + 9
				else:
					print("The field has to have 9 numbers")
					x = x + 9
		name_phone=input("Please introduce the description of the phone number: " )
		list_1.append(phone)
		list_1.append(name_phone)
		o=o+1
		list_2.append(list_1)
		if len()



	list_3.append(list_2)
	list_4.append(list_2)

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