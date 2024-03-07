*დავალება 1:*
for i in range(21):
    print(i)


*დავალება 2:*

sum = 0
for i in range(50, 101):
    sum += i
print(sum)

*დავალება 3:*

for i in range(-10, 11, 3):
    print(i)

*დავალება 4:*

num1 = int(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = int(input("შემოიტანეთ მეორე რიცხვი: "))

if num1 > num2:
    max_num = num1
    min_num = num2
else:
    max_num = num2
    min_num = num1

for i in range(min_num, max_num + 1, 2):
    print(i)

    დავალება 5 :

num1 = int(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = int(input("შემოიტანეთ მეორე რიცხვი: "))

start = min(num1, num2)
end = max(num1, num2)

sum = 0
for i in range(start, end + 1):
    sum += i

print(sum)