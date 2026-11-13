def flip(digit):
    if digit // 10 == 0:
        return digit

    last = digit % 10
    rest = flip(digit // 10)
    return last * pow(10, len(str(rest))) + rest

number = int(input("\nEnter a number : "))
guess = int(input(f"Guess what {number} will be when flipped : "))

print(f"\nFlipped Number : {flip(number)}\nYour Guess : {guess}")