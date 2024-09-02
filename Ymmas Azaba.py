#Program Name: Wk4_firstname_lastname.py
#Student Name: Ymmas Azaba
#Course: ENTD220
#Instructor: My instructor
#Date: 30/08/2024


print('BY: Ymmas Azaba')

# Addtional Function 

def add(n1, n2):
    return n1 + n2

# Substraction function
def sub(n1, n2):
    return n1 - n2

# Multplication function
def mul(n1, n2):
    return n1 * n2

# Division function
def div(n1, n2):
    # Division function with exception handling for division by zero
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

def checknum(num):
    # Check if the input is within the valid range using raise function
    if num < -10 or num > 20:
        raise ValueError("Number out of range")
    return num

# Main Program Loop

while True:
    try:
        # Get user inputs
        fnum = float(input("Enter first number between -10 and 20 --> "))
        fnum = checknum(fnum)  # Check if the first number is in range

        snum = float(input("Enter second number between -10 and 20 --> "))
        snum = checknum(snum)  # Check if the second number is in range

        # Perform the division operation
        result = div(fnum, snum)
        print("The result of division = ", result)
        break
    # except error to raise Cannot divide by zero
    except ValueError as e:
        print("Error -->", e)
        continue

print("Thank you for using the calculator!")
