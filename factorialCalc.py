#Factorial Calculator: Calculate factorial of a given number

number = int(input("Enter your number?:"))
answer = 1
for num in range(1,number+1):
    answer *= num

print(f"Factorial! = {answer}")