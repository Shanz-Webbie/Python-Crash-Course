message = input("Tell me something, and I will repeat it back to you.")
print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit' :
	message = input(prompt)
	print(message)

active = True
while active:
	message = input(prompt)

	if message == 'quit' :
		active = False

	else:
		print(message)