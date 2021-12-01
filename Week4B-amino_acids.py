# Dominic Pergola
# CSCI 102 - Section B
# Week 4 - Part B
# Reference: none
# Time ~ 15 min

#take inputs
print("Input the chemical elements of the amino acid:")
carbon = int(input("CARBON>"))
hydrogen = int(input("HYDROGEN>"))
nitrogen = int(input("NITROGEN>"))
oxygen = int(input("OXYGEN>"))
sulfur = int(input("SULFUR>"))

#test for acids using their differing elements and assign variable acid accordingly
if carbon == 3:
    if sulfur == 0:
        acid = "Alanine"
    else:
        acid = "Cysteine"
elif carbon == 6:
    if hydrogen == 14:
        acid = "Arginine"
    else:
        acid = "Histidine"
elif carbon == 4:
    acid = "Asparagine"
else:
    acid = "Glutamine"
    
#print outputs
print(f"The amino acid for {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S is {acid}")
print(f"OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S")
print(f"OUTPUT {acid}")
