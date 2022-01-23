magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

pets = ['ember', 'bart', 'maggie']
for pet in pets:
	print(pet)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

pets = ['ember', 'bart', 'maggie']
for pet in pets:
	print(f"{pet.title()}, I love you.")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone. That was a great magic show!")