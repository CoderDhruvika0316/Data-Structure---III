def mirror(digit):
    if digit == 0:
        return 0
    return digit * (digit + 1)

number = int(input("Enter a number : "))
guess = int(input(f"Guess what the mirror of {number} is : "))

print(f"\nMirror of {number} : {mirror(number)}\nYour guess : {guess}")