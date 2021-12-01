# Dominic Pergola
# CSCI 102 - Section H
# Week 2 - Part B
# Reference: none
# Time ~ 15 minutes

#ask for string
print("Please enter a string:")
the_str = input("STRING>")

#ask for bounds to slice the string and assign them to variables
print("Please enter 4 numbers to slice the string")
first_bound = int(input("A>")) + 1
second_bound = int(input("B>"))
third_bound = int(input("C>")) + 1
fourth_bound = int(input("D>"))

#output the sliced string
print("OUTPUT", the_str[first_bound:second_bound], the_str[third_bound:fourth_bound])
