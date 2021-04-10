# Try , Except

try:
    number = int(input('Input a number '))
    print(number)
except: 
    print("Invalid Input")



try:
    number = 10/0
    print(number)
except ZeroDivisionError: 
    print("Can not be divided by 0")
