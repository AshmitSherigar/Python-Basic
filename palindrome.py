# palindrome checker
palindrome = input("Enter your PALINDROME : ")

if palindrome == palindrome[::-1]:
    print(f"Yes {palindrome} is a palindrome")
else:
    print(f"No {palindrome} is a palindrome")