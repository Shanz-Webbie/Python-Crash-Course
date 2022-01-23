""" A class that can be used to represent a car."""
""" A set of classes used to represent gas and electric cars."""

class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 23

	def get_descriptive_name(self):
			"""Return a neatly formatted descriptive name."""
			long_name = f"{self.year} {self.make} {self.model}"
			return long_name.title()

	def increment_odomter(self, miles):
			"""Add the given amount to the odometer reading."""
			self.odometer_reading += miles

	def update_odometer(self, mileage):
		"""Set the odometer reading in a given value.
		Reject the change if it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(22)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odomter(100)
my_used_car.read_odometer()