requested_topping = 'mushrooms'

if requested_topping!= 'anchovies':
	print("Hold the anchovies")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'peperoni' in requested_toppings:
	print("Adding peperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'peperoni' in requested_toppings:
	print("Adding peperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


requested_toppings1 = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings1:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print (f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# Store information about piza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']} crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")


