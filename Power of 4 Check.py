def ispowerof4(digit):
    if digit <= 0:
        return False
    if digit == 1:
        return True
    if digit % 4 == 0:
        return ispowerof4(digit // 4)
    return False

number = int(input("Enter a number : "))
guess = input(f"Guess if {number} is a power of 4 or not (YES/NO) : ")

print(f"\nIs a Power of 4 : {ispowerof4(number)}\nYour Guess : {guess}")