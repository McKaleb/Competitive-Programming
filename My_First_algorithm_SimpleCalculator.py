def calculator():
	while True:
		try:
			x = float(input("Enter the first number: "))
			y = float(input("Enter the second number: "))
			if type(x) == float and type(y) == float:
				oper = input('Enter the operator: ')	
				if oper == "+":
					print(f'The sum of the two numbers is {x + y}.')
					break
				elif oper == "*":
					print(f'The product of the two numbers is {x * y}.')
					break
				elif oper == "/":
					print(f'The quotiet of the two numbers is {x / y}.')
					break
				elif oper == "-":
					print(f'The difference of the two numbers is {x - y}.')
					break
				else:
					print("You entered a wrong operator. Please try again!")
		except:
			print("I said numbers!")
	return
calculator()

def tryAgain():
	while True:
		try_again = input("Would you like to use the calculator again? (yes/no): ")
		if try_again.lower() == 'yes':
			calculator()
		elif try_again.lower() == 'no':
			break
		else: 
			print("Wrong input")
			tryAgain()
tryAgain()