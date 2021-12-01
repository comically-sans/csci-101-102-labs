# Dominic Pergola
# CSCI 102 - Section B
# Week 7 - Part A
# Reference: none
# Time ~ 15 min

print("How many rows does the checkerboard have?")
row_num = int(input("ROWS> "))

print("How many columns does the checkerboard have?")
column_num = int(input("COLUMNS> "))

print("Whate are the strings with which to pattern it?")
var1 = input("FIRST> ")
var2 = input("SECOND> ")

row1 = []
row2 = []
i = 0

for num in range(column_num):
    if i % 2 == 0:
        row1.append(var1)
        row2.append(var2)
    else:
        row1.append(var2)
        row2.append(var1)

    i += 1

print(f" A checkerboard with {row_num} rows, {column_num} columns, first string is {var1}, and second string is {var2} is:")

i = 0
for num in range(row_num):
    if i % 2 == 0:
        print("OUTPUT", row1)
    else:
        print("OUTPUT", row2)

    i += 1

print("And the 2D array representation is:")

board = []
i = 0
for num in range(row_num):
    if i % 2 == 0:
        board.append(row1)
    else:
        board.append(row2)

    i += 1

print("OUTPUT", board)
