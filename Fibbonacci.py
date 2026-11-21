def fibonacci(digit):
    if digit <= 1:
        return digit
    return fibonacci(digit - 1) + fibonacci(digit - 2)

number = int(input(f"Enter a number : "))
guess = int(input(f"Guess what the value of fibonacci({number}) is : "))

print(f"\nValue of Fibonacci({number}) : {fibonacci(number)}\nYour Guess : {guess}")