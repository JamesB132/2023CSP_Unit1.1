#   a114_divisible.py

# get two numbers from user

number = input("Enter a number ")
number2 = input("Enter another number ")

rem = int(number) % int(number2)
# loop while the numbers are not divisible (the remainder is not 0)
while(rem != 0):
    print("Not Divisible")
    number = input("Enter a number ")
    number2 = input("Enter another number ")

    rem = int(number) % int(number2)

if (rem == 0):
    print("Divisible")

# inform user of result

# gather user input again

# inform user of result