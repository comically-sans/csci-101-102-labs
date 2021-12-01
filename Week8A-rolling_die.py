# Dominic Pergola
# CSCI 102 - Section B
# Week 8 - Part A
# Reference: 
# Time ~  min


print("Input the number of sides of the die:")
sides = int(input("SIDES> "))
print("Input the number of rolls to make:")
rolls = int(input("ROLLS> "))
print("Input the seed for the random number generator:")
seed = int(input("SEED> "))

import random
random.seed(seed)
roll_list = []
for i in range (rolls):
    roll = random.randint(1, sides)
    roll_list.append(roll)

print(f"Your {rolls} rolls of a {sides}-sided die follow:")
i = 1
while i <= sides:
    side_total = roll_list.count(i)
    print(f"OUTPUT {i} occured {side_total} times")
    i += 1
