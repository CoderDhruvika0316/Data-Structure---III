def flip(word):
    if len(word) == 1:
        return word

    return flip(word[1:]) + word[0]

name = input("Enter your name : ")
guess = input(f"Guess what your name ({name}) will be when reversed : ")

print(f"\nFlipped Name : {flip(name)}\nYour Guess : {guess}")