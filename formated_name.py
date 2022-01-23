def get_formated_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)


def formated_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

new_name = formated_name('john', 'lee', 'hooker')
print(new_name)

def get_formated_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

	musician1 = get_formated_name('jimi', 'hendrix')
	print(musician1)

	musician2 = get_formated_name('john', 'hooker', 'lee')
	print(musician2)