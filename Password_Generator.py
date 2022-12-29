import random

#list of letters
letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
,'u','v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P'
,'Q','R','S','T','U','V','W','X','Y','Z']

#list of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#list of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '@', '+']

#Prints a wwelcome text
print('Welcome to the Password Generator')

#variables to store the number of letters, number or symbols in the password 
g_letters = int(input("How many letters would you like in your password,The sum of your letters, numbers, symbols should b e equal to 12:\n"))
g_symbols = int(input("How many symbols would you like in your password\n"))
g_numbers = int(input("How many numbers would you like in your password\n"))

#sum to get the total length of the inputs
sum = g_letters + g_symbols + g_numbers	

#function for generating password
def password_gen(g_letters, g_symbols, g_numbers):
	password_list = []
	password = ''
	for char in range(1, g_letters + 1):
		r_letter = random.choice(letters)
		password_list += r_letter

	for sym in range(1, g_symbols + 1):
		password_list += random.choice(symbols)

	for num in range(1, g_numbers + 1):
		password_list += random.choice(numbers)

	random.shuffle(password_list)


	for i in password_list:
		password += i

	print(password)

#makes sure password is 12 characters wrong
if sum == 12:
	password_gen(g_letters, g_symbols, g_numbers)
else:
	print('Your password should have 12 characters')
