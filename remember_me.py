import json

def get_stored_username():
	"""Get stored username, if available."""

	filename = 'username.json'

	try:
		with open(filename) as f:	
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def greet_user():
	"""Greet the user by name."""

	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:

# Load the username, if it had been stored previously.
# Otherwise, prompt for the username and store it.

			username = input("What is your name?")
			filename = 'username.json'
			with open(filename, 'w') as f:
				json.dump(username, f)
				print(f"We'll remember you when you come back, {username}!")
		
greet_user()