class Dog:
	""" A simple attempt to model a dog."""

	def __init__(self, name, age):
		""" Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		""" Simmulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
			""" Simmulate rolling over in response to a command."""
			print(f"{self.name} rolled over!")

my_dog = Dog('Bart', 1.5)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYou dog's name is {your_dog.name}.")
print(f"Your is {your_dog.age} years old.")
your_dog.roll_over()