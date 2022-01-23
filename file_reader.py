filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


	contents = file_object.read()
print(contents.rstrip())
