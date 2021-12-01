# Dominic Pergola
# CSCI 102 - Section B
# Week 4 - Part A
# Reference: none
# Time ~20 min

comp_name = input("Enter company name: ")
comp_loc = input("Enter company city/state: ")
cash_name = input("Enter cashier name: ")
item1 = input("Purchased item 1 name: ")
item1_price = float(input("Purchased item 1 price: "))
item2 = input("Purchased item 2 name: ")
item2_price = float(input("Purchased item 2 price: "))
item3 = input("Purchased item 3 name: ")
item3_price = float(input("Purchased item 3 price: "))
end = input("Enter your favorite ending message: ")

bar = "-----------------------------------"
double_bar = "==================================="
total = item1_price + item2_price + item3_price

print("        RECEIPT GENERATOR")
print(bar)
print(f"    {comp_name}")
print(f"    {comp_loc}")
print(double_bar)
print(f"    Your cahier was: {cash_name}")
print("    Welcome Valued Customer")
print(double_bar)
print("    Item Name       Item Price")
print("")
print(f"    {item1}        ${item1_price:.2f}")
print(f"    {item2}        ${item2_price:.2f}")
print(f"    {item3}        ${item3_price:.2f}")
print("")
print(double_bar)
print(f"    Total Cost of Order: {total:.2f}")
print(double_bar)
print(f"    {end}")
print(bar)
