#დავალება 1

numbers = [17, 25, 10, 42, 8, 36, 50, 29, 63, 5]


largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num



print("Largest number in the list:", largest)

#დავალება 2

numbers = list(range(30, 51))

odd_count = 0

# Count odd numbers
for num in numbers:
    if num % 2 != 0:
        odd_count += 1

print("Count of odd numbers:", odd_count)

#დავალება 3

multiples_of_4 = [num for num in range(10, 51) if num % 4 == 0]

multiples_of_4.reverse()

print("Reversed list of multiples of 4:", multiples_of_4)

#დავალება 4

numbers = list(range(50, 101))


for index, num in enumerate(numbers):
    if num % 2 == 0:
        print(f"{num}-{index}", end=" ")
