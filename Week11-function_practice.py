#Dominic Pergola
#CSCI 102-Section B
#Week 11 Lab
#References: EDUCBA for trig functions
#Time: 20 minutes

import math

#print_output
def print_output(input_str):
    return print(f"OUTPUT {input_str}")

#triangle_hypotenuse
def triangle_hypotenuse(num1, num2):
    side = math.sqrt((float(num1) ** 2) + float(num2) ** 2)
    print_output(f"{side:.2f}")
    return

#feet_to_meters
def feet_to_meters(feet):
    meters = float(feet) * 0.3048
    print_output(f"{meters:.4f}")
    return

#polar_coords
def polar_coords(x_val, y_val):
    triangle_hypotenuse(x_val, y_val)
    angle = math.degrees(math.atan(float(y_val) / float(x_val)))
    print_output(f"theta: {angle:.2f}")
    return

#dollars_to_euros
def dollars_to_euros(dollars):
    euros = float(dollars) * 0.86
    print_output(f"{euros:.2f}")
    return
