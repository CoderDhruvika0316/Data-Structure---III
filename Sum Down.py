def sumdown(digit):
    if digit == 1:
        return 0
    else:
        return digit + sumdown(digit - 1)

number = int(input("\nEnter a number :"))
guess = int(input(f"Guess what is the result of [sumdown({number})] :"))

print(f"\nResult :-\n-> [sumdown({number})] : {sumdown(number)}\n-> Your Guess : {guess}")