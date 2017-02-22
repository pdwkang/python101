# Dictionary is fancy python term for a JS object
# Must put keys (properties) in ""
# Called key-value pairs in python (property, value)

zombie = {
	'speed': 10,
	'power': 6,
	'hunger': 12,
	'name' : 'Zombie'
}

print zombie['speed']
# print zombie[0]

# add a new key just like you do in JS. vars are dynamic in Python!
zombie['weapon'] = "Fist";
zombie['startX'] = 200;
zombie['startY'] = 100;
print zombie;


# Change the value of an existing key just like JS
if zombie['speed'] < 5:
	zombie['position'] = zombie['startX'] + 2;
elif zombie['speed'] < 10:
	zombie['position'] = zombie['startX'] + 4;
else:
	zombie['position'] = zombie['startX'] + 6;

# you can delete a key with del
zombie['pointless'] = 'duh'
del zombie['pointless']
print zombie;

# Store all the techs we know in a dictionary and set the value from 1-10
skill1 = 'Redux'
techs = {
	'javascript' : 9,
	'jQuery' : 8,
	'React.js' : 10,
	'Redux' : 8,
	'node' : 1,
	'express' : 3,
	'MySql' : 4,
	'css' : 9,
	'sass' : 8,
	'html' : 9,
	skill1: 7
}
print techs

# for loops through dictionaries start with key (placeholder), value
for key,value in techs.items():
	print key,value;

if zombie.has_key('mother_name'):
	print zombie['mother_name']

for key in zombie:
	print zombie[key]

# just like in JS, you can put dictionaries inside of lists (objects in arrays)
zombies = []; #an empty list called zombies
zombies.append({
	'speed':10,
	'power':6,
	'hunger':5,
	'name':'Bill'
})

zombies.append({
	'speed':5,
	'power':16,
	'hunger':9,
	'name':'Sven'
})

print zombies

# prints first zombie's name
print zombies[0]['name']

# this is like the map function
for zombie in zombies:
	print zombie['name'];

# just like JS objects, you can assign a list to a dictionary key
zombies[0]['victims'] = [{}, 'rishi', 'anna']
print zombies[0]
zombies[0]['victims'][0]['name'] = 'Sean'

print zombies[0]['victims'][0]['name']

zombies[0]['at_night'] = {
	'power' : 23,
	'hunger': 20,
	'weapon': 'baseball bat'
}

