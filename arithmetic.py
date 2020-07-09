 #  Write a user driven program which will will ask users to input two no and perform somecalculation
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform")
char = input("Enter any  one of these char for specific operation +,*,/,- : ")

if char == '+':
    result = num1 + num2
elif char == '*':
    result = num1 * num2
elif char == '/':
    result = num1 / num2
elif char == '-':
    result = num1 - num2
else:
    print("Input character is not valid")

print(num1, char , num2, ":", result)