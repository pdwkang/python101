from rpg_hero import Hero;
# import hero .. hero = hero.Hero;
from rpg_monsters import Goblin;

# Hero() is an class (or object) imported from rpg_hero
hero = Hero();
enemies = [Goblin(), Goblin()];

for enemy in enemies:
	# loop through all the bad guys in the enemies list
	# print vars(enemy)
	while hero.alive() > 0 and enemy.alive():
		print "What will you do?";
		print "1. Fight %s" % enemy.name
		print "2. Run away from %s" % enemy.name
		print "> ",
		input = int(raw_input());
		if input == 1:
			# user has chosen to fight
			# subtarct health from enemy = hero power
			# enemy.health -= hero.power;
			hero.attack(enemy);
		elif input == 2:
			# user has chosen to run away, break out of while loop
			break;
		else:
			# user has malfunctioned. complain
			print "Invalid choice %r" % input
		if enemy.alive():
			hero.health -= enemy.power
	
	print "Enemy health : %s" % enemy.health
	print "Hero health : %s" % hero.health
	if hero.alive():
		# we know they won, because enemy.health is not > 0
		print "You won! the %s is defeated" % enemy.name
	else:
		print "you were defeated by the ferocious %s" % enemy.name