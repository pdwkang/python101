# print 1 to 10
for i in range(1,11):
	print i


# print from start to end(user input)
# start = int(raw_input("Start from: "))
# end = int(raw_input("End on: "))
# for i in range(start,end):
# 	print i


# print each odd number b/t 1 and 10 inclusive
for i in range(1,11):
	if i%2 == 1:
		print i;


# print 5x5 square of * characters
# size = 5
# for i in range(0, size):
# 	print '*' * size

# print N x N square of * characters. promt user for N

# square_size = int(raw_input("How big is the square?: "))
# for i in range(0, square_size):
# 	print '*' * square_size;



#Given a height and width, input by user, make a empty box
height = int(raw_input("height?: "));
width = int(raw_input("width?: "));

for i in range(height):
	if i == 0:
		print '*' * width;
	elif i == height-1:
		print '*' * width;
	else:
		empty_space = ' '
		between = '*' + empty_space * (width - 2) + '*'
		print between;