# Basic Password Generator:  Create random passwords with random characters and digits and symbols.
import random
import string

password_length = int(input("Enter the length of the password?: "))
symbol = input("Do you want symbols?(y or n):")

password = ''

character_with_symbol = string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits 
character_without_symbol = string.ascii_lowercase  + string.ascii_uppercase + string.digits 

def random_generator(characters):
    global password
    for alp in range(password_length):
        num = random.randint(0,len(characters))
        password += characters[num]
    print(f"Your Password is : {password}")

if symbol.lower() == "y":
    random_generator(character_with_symbol)
elif symbol.lower() == "n":
    random_generator(character_without_symbol)
else:
    print("Invalid Operation")







