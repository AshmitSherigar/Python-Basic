operator = input("Enter the operation you want to perform?:")

num1 = float(input('Enter your first number?:'))
num2 = float(input('Enter your second number?:'))

if operator == '+':
    print('You Have Choosen ADDITION')
    print(num1 + num2)
elif operator == '-':
    print('You Have Choosen SUBTRACTION')
    print(num1 - num2)
elif operator == '*':
    print('You Have Choosen MULTIPLICATION')
    print(num1 * num2)
if operator == '/':
    print('You Have Choosen DIVISION')
    if num2 == 0:
        print("Zero Division , Swapping the numbers")
        print(num2/num1)
    else:
        print(num1/num2)
elif operator == '//':
    print('You Have Choosen FLOOR DIVISION')
    if num2 == 0:
        print("Zero Division , Swapping the numbers")
        print(num2//num1)
    else:
        print(num1//num2)
elif operator == '%':
    print('You Have Choosen REMAINDER')
    if num2 == 0:
        print("Zero Division , Swapping the numbers")
        print(num2%num1)
    else:
        print(num1%num2)
elif operator == '**':
    print('You Have Choosen Power')
    answer = input("Is the First Num BASE and Second Num EXPONENTS (Y/N)")
    if answer == 'Y':
        print(num1**num2)
    if answer == 'N':
        print(num2**num1)
else:
    print("You Have Choosen WRONG operators")
    print("Here is a list of them , (+ - * /  // % **)")
