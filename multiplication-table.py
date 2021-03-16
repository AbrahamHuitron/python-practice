print("Hello, welcome to the multiplication table program.")
number1 = int(input("Please enter the number which you'd like to see: "))
number2 = int(input("Now enter the amount of calculations you'd like to see: "))

for i in range(1, number2 + 1):
    print(number1, " * ", i, " = ", number1 * i)
    i + 1