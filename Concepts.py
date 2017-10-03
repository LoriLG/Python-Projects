# Assign an integer to a variable
number = 2

# Assign a string to a variable
city = "Portland"

# Assign a float to a variable
decimal = 7.52

# Use the print function and .format()notation to print out the variables you assigned
print (" The assigned integer is {}.\n The string is {}.\n The float number is {}."
       .format(number,city,decimal))

# Use the following operators: +,-,*,/,+=,=,%
def math_functions():
    add = number + decimal
    subtract = decimal - number
    multiply = number * decimal
    divide = decimal/number
    remainder = decimal % number
    concatenate = 0
    concatenate += 1

    print ("\nadd = {}, subtract = {}, multiply = {}, divide = {}, \nremainder = {}, and concatenate = {}.".format(add,subtract,multiply,divide,remainder,concatenate))
    
math_functions()

# Use of logical operators: and, or, not
def operators():
    x = 5
    y = 10
    
  
    if x and y < 7:
        print " \n x and y are both less than 7"
    if x or y < 7:
        print " \n either x or y is less than 7"
    if not y < 7:
        print "\n y is not less than 7"
    

operators()

# Use of condittional statements: if, elif, else, and a while loop
def new_name():
    name = ""
    stop = True
    while stop:
        name = raw_input("\nWhat is your first name? ").lower().capitalize()
        if name == 'John':
            print "\nHello John. Welcome to the world of Software Developers.\n"
        elif name == 'Charlie':
            print "\nHello Charlie. Welcome to the world of Martial Arts.\n"
        else:
            print "\nHello. Have a wonderful day!\n"
            
        stop = False
                
new_name()

# Use of a for loop

for num in range(5,10):
    print num

# Create a list and iterate through the list using a for loop
# to print each item out on a new line.

animals = ['dogs','cats', 'horses', 'birds', 'pigs', 'monkeys']
for animal in animals:
    print animal

# Create a tuple and iterate through it using using a for loop
# to print each item out on a new line
grades = (100,95,88,'B','A')
for grade in grades:
    print grade

# Define a function that returns a string variable

breakfast = "cereal and eggs"
lunch = "soup and a sandwich"
dinner = "meat, starch, and a vegetable"

def food_choice(breakfast,lunch,dinner):
    return breakfast,lunch,dinner

    
# Call the function you defined above and print the result to the shell
food_choice(breakfast,lunch,dinner)
print("\nThis is what you can have for breakfast: {},\nfor lunch: {},\nand for dinner: {}."
          .format(breakfast,lunch,dinner))


    
    
