calculation = [int(number) for number in input("\nEnter 3 numbers seperated by spaces : ").split()]

guess = int(input("\nGuess what the head of the numbers you have entered is : "))
guessed = input("Guess what the tail of the numbers you have entered is : ")

print(f"\nHead : {calculation[0]}\nYour Guess : {guess}\n\nTail : {calculation[1:]}\nYour Guess : {guessed}")