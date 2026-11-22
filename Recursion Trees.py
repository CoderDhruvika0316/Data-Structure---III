def ways(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return ways(rows - 1, columns) + ways(rows, columns - 1)

digit = int(input(f"Enter the grid size for both rows and columns : "))
guess = input(f"Guess what ways({digit}, {digit}) is : ")

print(f"Ways({digit}, {digit}) : {ways(digit, digit)}\nYour Guess : {guess}")