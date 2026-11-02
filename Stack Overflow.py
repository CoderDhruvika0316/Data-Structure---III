def sumdown(digit):
    if digit == 0:
        return 0
    else:
        return number + sumdown(digit - 1)

number = int(input("Enter a number : "))
print(sumdown(number))