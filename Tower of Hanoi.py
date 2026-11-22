def hanoi(digit):
    if digit == 0:
        return 0
    return 2 * hanoi(digit - 1) + 1

number = int(input("Enter a number : "))
guess = int(input(f"Guess what hanoi({number}) is : "))

print(f"\nHanoi({number}) : {hanoi(number)}\nYour Guess : {guess}")