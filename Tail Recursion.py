def tail(digit, numeral = 0):
    if digit == 0:
        return numeral
    return tail(digit - 1, numeral + digit)

number = int(input("Enter a number : "))
guess = int(input(f"Guess what the tail sum of {number} is : "))

print(f"\nTail sum of {number} : {tail(number)}\nYour Guess : {guess}")