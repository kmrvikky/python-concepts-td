#WAP to Calculate Factorial Using a Function 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
fact = factorial(number)
print(f"Factorial of {number} is: {fact}")
