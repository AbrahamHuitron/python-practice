# Sample calculator project
# https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

# Define our welcome function
def welcome():
    print('''
    Welcome to Calculator
    ''')

# Adding the welcome() function to the beginning of the code
welcome()

# Define our function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))

    if operation == '+':
        # Addition
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        # Substraction
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        # Multiplication
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        # Division
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
calculate()