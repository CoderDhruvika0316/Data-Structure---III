def counter(digit, first = 0, second = 0):
    if first == digit and second == digit:
        return 1
    total = 0
    if first > second:
        total += counter(digit, first, second + 1)
    if first < digit:
        total += counter(digit, first + 1, second)
    return total


number = input("Enter a number : ")
guess = int(input(f"Guess what counter({number}) is : "))

print(f"\nCounter(number) : {counter(int(number))}\nYour Guess : {guess}")