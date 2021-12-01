# Dominic Pergola
# CSCI 102 - Section H
# Week 3 - Part B
# Reference: simple calculator lab code
# Time ~20 minutes

print("Welcome to our Enhanced Calculator")

#ask for inputs
print("Please input a real number")
operand_one = float(input("FIRST> "))
print("Please input another real number")
operand_two = float(input("SECOND> "))
print("")
print("Choose one of the following operations:\n 1 - addition\n 2 - subtraction\n 3 - multiplication\n 4 - division")
opp = int(input("OPERATION> "))
print("")

#carry out operands and print results
if opp == 1:
    sum_ = operand_one + operand_two
    print(f"The result of the addition is: {sum_:.6f}\nOUTPUT {sum_:.6f}")
elif opp == 2:
    difference = operand_one - operand_two
    print(f"The result of the subtraction is: {difference:.6f}\nOUTPUT {difference:.6f}")
elif opp == 3:
    product = operand_one * operand_two
    print(f"The result of the multiplication is: {product:.6f}\nOUTPUT {product:.6f}")
elif opp == 4:
    quotient = int(operand_one / operand_two)
    remainder = int(operand_one % operand_two)
    print(f"The result of the division is: {quotient} (quotient) and {remainder} (remainder)\nOUTPUT {quotient}\nOUTPUT {remainder}")
else:
    print("This does not compute")
    print("dumbass")

print("Thank you for using our calculator.")
