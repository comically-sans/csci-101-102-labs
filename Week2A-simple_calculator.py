# Dominic Pergola
# CSCI 102 - Section H
# Week 2 - Part A
# Reference: Chase Lampe helped me with rounding on the f-string
# Time ~ 1 hour

#initialize values at zero
operand_one = 0.0
operand_two = 0.0
sum_ = 0.0
difference = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

#ask for inputs
print("Please input a real number")
operand_one = float(input("FIRST>"))
print("Please input another real number")
operand_two = float(input("SECOND>"))

#carry out operations
sum_ = operand_one + operand_two
difference = operand_one - operand_two
product = operand_one * operand_two
quotient = int(operand_one / operand_two)
remainder = operand_one % operand_two

#print results
print(f"The sum of {operand_one} and {operand_two} is {sum_:.1f}\nOUTPUT {sum_:.1f}")
print(f"The difference of {operand_one} and {operand_two} is {difference:.1f}\nOUTPUT {difference:.1f}")
print(f"The product of {operand_one} and {operand_two} is {product:.1f}\nOUTPUT {product:.1f}")
print(f"The quotient of {operand_one} and {operand_two} is {quotient}\nOUTPUT {quotient}")
print(f"The remainder of {operand_one} and {operand_two} is {remainder:.2f}\nOUTPUT {remainder:.2f}")
