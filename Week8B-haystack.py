# Dominic Pergola
# CSCI 102 - Section B
# Week 8 - Part B
# Reference: none
# Time ~ 20 min

print("Enter a DNA string s:")
s = input("s> ")
print("Enter a substring t:")
t = input("t> ")

if len(t) <= len(s):
    index_list = []
    counter = 0
    i = 0
    for letter in range(len(s)):
        if s[i : i + len(t)] == t:
            counter += 1
            index_list.append(str(i+1))
        i += 1

    index_string = ' '.join(index_list)
    print(f"The total number of substrings found is {counter}")
    print(f"OUTPUT {counter}")
    print(f"The locations of these substrings in s are: {index_string}")
    print(f"OUTPUT {index_string}")

else:
    print("Error: Substring is longer than DNA string")
    print("OUTPUT ERROR")
