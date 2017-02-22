# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
fullName = 'Paul Kang'
age = '27'


# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.
myArray = []
myArray.extend([fullName, age])
print myArray


# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.
def sayHello():print "hello"
sayHello();


# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.
splitName = fullName.split(' ')
print splitName


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)
def sayName(name):print "Hello, " + name + "!"
sayName(splitName[0]);

# def say_name():
# 	print "Hello, {}".format(split_name[0])
# say_name()	




# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp
def myAge(year):
	age = 2017 - year;
	print age;
myAge(1988)



# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  
# Don't forget to call the function!
# HINT: Consider using a 'for loop'.

def sum_odd_numbers(max):
	sum = 0
	for i in range(1,max):
		if i % 2 != 0:
			sum += i
	print sum

sum_odd_numbers(5001)
# print sum
# function sum_odd_numbers() {
#     var sum = 0;
 

#     // Write your code here
#     console.log(sum);
# }

 # for loop is [for] [what_you_call_this_one] [var] [in] 
# for students in dc_class_as_array: print students
	# Indentation matters in python
# for i in range(1,10) : print dc_class
