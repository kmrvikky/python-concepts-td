#Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)
 

import math

# Step 1: Ask the user for a number
number = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)  

# Step 3: Display the results
print(f"Square root: {sqrt_result}")
print(f"Logarithm: {log_result}")
print(f"Sine: {sine_result}")
