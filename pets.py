pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)


def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'bart')
describe_pet('hamster', 'harry')
describe_pet(animal_type = 'cat', pet_name = 'ember')

def describe_pet(pet_name, animal_type='dog'):
	"""Display information about pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='bart')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

