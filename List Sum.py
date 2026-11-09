def listsum(listed):
    if listed == []:
        return 0
    return listed[0] + listsum(listed[1:])

sequence = [int(number) for number in input("\nEnter four numbers separated by spaces : ").split()]
guess = int(input("Guess what the list sum of the numbers you have entered is : "))

print(f"\nList Sum : {listsum(sequence)}\nYour Guess : {guess}")