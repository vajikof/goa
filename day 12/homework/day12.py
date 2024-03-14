Sure, here are the Python implementations for each of the algorithms:

1. Determine the sign of a number:

def sign_of_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# Example usage:
number = float(input("Enter a number: "))
sign_of_number(number)

2. Kilometer-mile or mile-kilometer conversion:

def convert_distance():
    operation = input("Choose an operation: 1. Kilometer to Mile, 2. Mile to Kilometer: ")
    value = float(input("Enter the numerical value to convert: "))
    
    if operation == '1':
        result = value * 0.621371  # Convert kilometers to miles
        print("Result:", result, "miles")
    elif operation == '2':
        result = value * 1.60934  # Convert miles to kilometers
        print("Result:", result, "kilometers")
    else:
        print("Wrong decision")

# Example usage:
convert_distance()

3. User registration algorithm:

def user_registration():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    
    print("Registration Successful")
    print("Name: {}, Age: {}, Email: {}".format(first_name + " " + last_name, age, email))

# Example usage:
user_registration()

4. Calculate the arithmetic mean of three numerical values:

def arithmetic_mean():
    numbers = [float(input("Enter a number: ")) for _ in range(3)]
    mean = sum(numbers) / len(numbers)
    print("Arithmetic mean:", mean)

# Example usage:
arithmetic_mean()

5. Output multiples of a number within a range:

def output_multiples():
    number = int(input("Enter a number from 1 to 9: "))
    for i in range(1, 51):
        if i % number == 0:
            print(i)

# Example usage:
output_multiples()

6. Output the cube of numbers in a range:

def output_cubes():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    start = min(num1, num2)
    end = max(num1, num2)
    for i in range(start, end + 1):
        print(i**3)

# Example usage:
output_cubes()

7. Calculate the sum of digits in a number:

def sum_of_digits():
    number = input("Enter a number: ")
    total = sum(int(digit) for digit in number)
    print("Sum of digits:", total)

# Example usage:
sum_of_digits()