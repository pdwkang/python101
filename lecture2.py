# # array is great, but its changeable! what if you wanted something
# # that wasnt changeable to keep programmers from breaking your code
# # or u just watned to be functional

a_tuple = (1,3,8)
print a_tuple;
print a_tuple[2];

# # loop through tuples the same way you do lists

# for number in a_tuple:
# 	print number

# teams = ('falcons', 'hawks', 'atl_united', 'silverbacks');
# for team in teams:
# 	if team == 'hawks':
# 		print 'Go Hawks!';
# 	else:
# 		print "Its Basketball season"

# team_a = "Falcons";
# # print team_a == "Falcons"

# # Or and And work the same way, just ()
# team_b = 'Braves'
# cond1 = team_a == 'Falcons'
# cond2 = team_b == 'Braves'
# if cond1 and cond2:
# 	print 'ATLLLLLL'

# # Pythons version of indexof is simply 'in'
# print 'hawks' in teams

# for team in teams:
# 	if team == 'hawks':
# 		print 'Go Hawks!';
# 	elif team == 'falcons':
# 		print 'sad super bowl';

# if 'hawks' in teams:
# 	print 'Go Hawks';
# elif 'falcons' in teams:
# 	print "go falcons";


# height = raw_input("How tall are you? (in inches)")
# if int(height) >= 42:
# 	print "You're tall enough"
# else:
# 	print "try the kiddie coaster"

# while loop
current = 1 
while (current < 10):
	print current;
	current+=1;

answer = 'play'
while answer != 'quit':
	answer = raw_input("Say quit, to stop the game!\n")