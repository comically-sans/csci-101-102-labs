# Dominic Pergola
# CSCI 102 - Section B
# Week 5 - Part B
# Reference: none
# Time ~20 minutes

#input for empties
print("Enter the number of empty bottle in Blaster's possession at the start of the day.")

empties = int(input("EMPTIES> "))

#input for found
print("Enter the number of empty bottles that Blaster found during the day.")

found = int(input("FOUND> "))

#input for cost
print("Enter the number of empty soda bottles required to buy a new soda.")

cost = int(input("COST> "))

#combine bottles and creat soda_drank variable
empty_bottles = empties + found
soda_drank = 0


while empty_bottles >= cost:

#floor divide bottles by cost to see what Blaster can afford and find remainder to see what's left
    new_soda = empty_bottles // cost
    leftover = empty_bottles % cost

#add new sodas bought to soda_drank variable
    soda_drank = soda_drank + new_soda

#reset bottles to remainder + soda bought    
    empty_bottles = new_soda + leftover

#print output
print("The total number of sodas that Blaster drank is:")
print(f"OUTPUT {soda_drank}")
