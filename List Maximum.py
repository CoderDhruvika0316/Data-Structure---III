def maximum(list):
    if len(list) == 1:
        return list[0]

    tail = maximum(list[1:])
    return list[0] if list[0] > tail else tail

numbers = input(f"Enter a list of numbers seperated by spaces : ")

elements = [int(number) for number in numbers.split()]

guess = int(input(f"Guess what the largest number in {elements} is : "))

print(f"\nLaregst : {maximum(elements)}\nYour Guess : {guess}")