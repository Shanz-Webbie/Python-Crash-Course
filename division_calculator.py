print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	try:
		second_number = input("\nSecond number: ")
		if second_number == 'q':
			break
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)