#  Binary Generator:  Gives the Binary value for the given integer

number = int(input("Enter your value to be converted to binary?: "))
rev_binary = ''

def int_to_binary(num):
    global number,rev_binary
    while True:

        remainder = number % 2 
        number = number // 2

        if number == 0:

            remainder = str(remainder)
            rev_binary+=remainder

            break
        else:

            remainder = str(remainder)
            rev_binary+=remainder


    print(f"So your number is {int(rev_binary[::-1])} in binary")

if number < 0 :
    print("Your Number won't be calculated well by the computer")

else:
    print(f"Oh you want to convert {number} to binary")
    int_to_binary(number)


