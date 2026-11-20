def methods(steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    return methods(steps - 1) + methods(steps - 2)

number = int(input("Enter a number : "))
print(f"\nSTORY :-\nCody has been sucked into a video game and his only way out is to find out all the different methods he can climb up the {number} stairs.")

guess = int(input(f"Guess how many methods Cody will have to figure out : "))

print(f"RESULT :-\nCody Correct Answer : {methods(number)}\nYour Guess : {guess}")