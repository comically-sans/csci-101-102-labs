# Dominic Pergola
# CSCI 102 - Section B
# Week 5 - Part A
# Reference: none
# Time ~20 minutes

print("Enter values to add. Enter quit when done.")

#create new list
new_list = []

#run loop until quit is entered
while True:
    num = input("NUMBER> ")

    if num == 'quit':
        break
    else:
        new_list.append(int(num))

#take in list variables
list_len = len(new_list)
list_sum = sum(new_list)

#print results
print(f"The addition of the {list_len} numbers entered is:")
print(f"OUTPUT {list_len} numbers")
print(f"OUTPUT {list_sum} total")
