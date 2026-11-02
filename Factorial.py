def factorial(digit):
    if digit == 0 or digit == 1:
        return 1
    else:
        return digit * factorial(digit - 1)

number = int(input("Enter a number : "))
guess = int(input(f"Guess what the value of {number}! is : "))

print(f"\nResult :-\n-> {number}! : {factorial(number)}\n-> Your Guess : {guess}")