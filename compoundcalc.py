principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter Your Principle Amount?:"))
    if principle < 0:
        print("You can't have less than zero as a principle amount!")
        principle = float(input("Enter Your Principle Amount?:"))
    else:
        break

while True:
    rate = float(input("Enter Your Intrest Rate?:"))
    if rate < 0:
        print("You can't have less than zero as a Intrest Rate!")
        rate = float(input("Enter Your Intrest Rate?:"))
    else:
        break

while True:
    time = int(input("Enter Your Time (in years)?:"))
    if time < 0:
        print("You can't have less than zero as a Time (in years)!")
        time = int(input("Enter Your Time (in years)?:"))
    else:
        break



total = principle + pow(( 1 + (rate/100) ),time)
print(f"Your Intrest after {time}years is ${total}")