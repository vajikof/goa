Here are the solutions to your tasks:

1. *Check whether it is odd or even:*
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

2. *Temperature Classification:*
temp = float(input("Enter the temperature in Celsius: "))
if temp > 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
else:
    print("Cold")

3. *Letter Grading:*
score = int(input("Enter your exam score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

4. *Check Division:*
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif num % 2 == 0:
    print("The number is divisible by 2.")
elif num % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by either 2 or 3.")

5. *Comparing Numbers:*
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")



    Here are the solutions using while loops:

1. *Timer:*
count = 10
while count > 0:
    print(count)
    count -= 1
print("Time is up.")

2. *Sum of Numbers:*
sum = 0
num = int(input("Enter a number (enter 0 to stop): "))
while num != 0:
    sum += num
    num = int(input("Enter a number (enter 0 to stop): "))
print("Sum of all the numbers entered:", sum)

3. *Password Verification:*
password = "12345678"
entered_password = input("Enter the password: ")
while entered_password != password:
    print("Incorrect password.")
    entered_password = input("Enter the password: ")
print("Password accepted.")

4. *Even Numbers:*
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

5. *Positive Numbers:*
sum = 0
num = float(input("Enter a positive number (enter a negative number to stop): "))
while num >= 0:
    sum += num
    num = float(input("Enter a positive number (enter a negative number to stop): "))
print("Sum of all positive numbers entered:", sum)


  
   
    
     
      
       
        
