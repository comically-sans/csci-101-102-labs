# Dominic Pergola
# CSCI 102 - Section H
# Week 6 - Part B
# Reference: none
# Time ~20 minutes

#take count input
print("How many numbers am I estimating John?")
count = int(input("COUNT> "))

#append each number to a list by iterating through as many times as the count
num_list = []
print("Input each number to estimate.")
for index in range(count):
    num_list.append(float(input("NUMBER> ")))

print("The square roots are as follows:")

#while i is less than the amount of numbers...
i = 0
while i < count:

    #run through the operation once with initial_guess as 10
    initial_guess = 10.0
    better_guess = (initial_guess + num_list[i] / initial_guess) / 2
    iteration = 1
    
    #run through the operation until initial_guess = better_guess, keeping track of the iterations through
    while initial_guess != better_guess:
        initial_guess = better_guess
        better_guess = (initial_guess + num_list[i] / initial_guess) / 2
        iteration += 1

    #once they're equal, print out the number with its corresponding better_guess and iteration value
    print(f"OUTPUT After {iteration} iterations, {num_list[i]}^0.5 = {better_guess:.3f}")

    i += 1
        
