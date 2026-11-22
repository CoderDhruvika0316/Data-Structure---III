keys = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}


def counter(digit):
    if len(digit) == 0:
        return 1
    return len(keys[digit[0]]) * counter(digit[1:])

number = input(f"Enter any set of digits from 2 - 9 (e.g. 2345, 678) : ")
guess = input(f"Guess what counter({number}) is : ")

print(f"\nCounter(number) : {counter(number)}\nYour Guess : {guess}")