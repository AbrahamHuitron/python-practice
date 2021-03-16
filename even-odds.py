# Hello, this program will check for evenor odds
print("Hello, welcome to the Even-Odds program!")
print("We will begin by having you enter a number.")

number = int(input("Enter your desired number: "))

if (number % 2) == 0:
    print("This number is even!")
else:
    print("This number is odd!")