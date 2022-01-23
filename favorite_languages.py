favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_laguages ['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_laguages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")


favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in favorite_laguages.keys():
	print(name.title())


favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah',]
for name in favorite_laguages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_laguages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

if 'erin' not in favorite_laguages.keys():
	print("Erin, please take our poll!")

favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in sorted(favorite_laguages. keys()):
	print(f"{name.title()}, thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in favorite_laguages.values():
	print(language.title())

favorite_laguages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("The following languages have been mentioned:")
for language in set(favorite_laguages.values()):
	print(language.title())

favorite_laguages = {
	'jen': ['python', 'ruby'],
	'sarah':['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_laguages.items():
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")

