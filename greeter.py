username = input("Please enter your name: ")
print(f"\nHello, {username}!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

username = input(prompt)
print(f"\nHello, {username}!")

def greet_user(username):
	"""Display a simple greeting."""
print(f"Hello, {username.title()}!")

greet_user('Shannon')

def get_formatted_name(first_name, last_name):
	""""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

# This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First_name: ")
	if f_name == 'q'
		break
	l_name = input("Last name: ")
	if l_name == 'q'
		break
		
	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")