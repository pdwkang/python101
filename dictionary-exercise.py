phonebook_dict = {
	'Alice': '703-493-1834',
	'Bob': '857-384-1234',
	'Elizabeth': '484-584-2923'
}

# Print Elizabeth's phone number.
# print phonebook_dict['Elizabeth']

# Add a entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'

# Delete Alice's phone entry.
del phonebook_dict['Alice']

# Change Bob's phone number to '968-345-2345'.
phonebook_dict['Bob'] = '968-345-2345'

# Print all the phone entries.
# print phonebook_dict

ramit = {
	'name': 'Ramit',
	'email': 'ramit@gmail.com',
	'interests': ['movies', 'tennis'],
	'friends': [
		{
			'name': 'Jasmine',
			'email': 'jasmine@yahoo.com',
			'interests': ['photography', 'tennis']
    	},
    	{
			'name': 'Jan',
			'email': 'jan@hotmail.com',
			'interests': ['movies', 'tv']
		}
	]
}

# Write a python expression that gets the email address of Ramit.
# print ramit['email']
# Write a python expression that gets the first of Ramit's interests.
# print ramit['interests'][0]
# Write a python expression that gets the email address of Jasmine.
# print ramit['friends'][0]['email']
# Write a python expression that gets the second of Jan's two interests.
# print ramit['friends'][1]['interests'][1]


# Letter Summary
def letter_histogram(string):
	output = {}
	for i in string:
		if i in output:
			output[i] += 1
		else:
			output[i] = 1
	print output

letter_histogram('banana')




# Word Summary
def word_histogram(long_string):
	string_to_array = long_string.lower().split(' ')
	output = {}
	for i in string_to_array:
		if i in output:
			output[i] += 1
		else:
			output[i] = 1
	print output	

word_histogram('To be or not to be')




