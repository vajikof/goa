#შემდეგი კოდი შეგიძლიათ გაუშვათ, როგორც სწორი პირველი ნაწილის გაშვების შემდეგ, 
#ასევე შეგიძლიათ გააკეთოთ ეკრანზე გამოსახვის მისაღებად, როგორც ეს მაგალითია:

numbers = []

# პირველი ნაწილი
for i in range(50,60+1):
    numbers.append(i)

# მეორე ნაწილი
even_numbers = []

for index in range(0, len(numbers)):
    if numbers[index] % 2 == 0:  # კორექტული პარამეტრების გამოყენება
        even_numbers.append(str(numbers[index]) + "-" + str(index))

print(numbers)
print(even_numbers)

Paint #ში განახლებული ალგორითმის გასაშვებად მივიღებთ შემდეგ გამოსახულებას:

1. #შექმენით მასივი numbers, რომელშიც განვსაზღვრავთ 50-დან 60-მდე ყველა რიცხვს.
2. #შექმენით ცარიელი მასივი even_numbers, რომელშიც ვინახავთ ლუწ რიცხვებს და მათი ინდექსების ნამბერებს.
3. #გამოიტანეთ მთელი numbers მასივი და even_numbers მასივი ეკრანზე.

#შემდეგ, როდესაც გამოვიყენებთ Paint-ს, შეგიძლიათ შექმნათ გამოსახულება,
#რომელშიც იქვე წერია რიცხვები და მათი ინდექსები. 
#შემდეგ, შეინახეთ გამოსახულება და გამოიტანეთ სურათა ფაილში.



1. #ნამრავლის გამოთვლა:

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# სიაში შემთხვევაში:
my_list = [1, 2, 3, 4, 5]
print("სიას ყველა ელემენტის ნამრავლია:", multiply_list(my_list))

2. #უარყოფითი რიცხვების ამოღება:

def get_negative_numbers(lst):
    result = [num for num in lst if num < 0]
    return result

# სიაში შემთხვევაში:
my_list = [1, -2, 3, -4, 5, -6]
print("უარყოფითი რიცხვები:", get_negative_numbers(my_list))

3. #საშუალოს პოვნა:

def average_of_list(lst):
    return sum(lst) / len(lst)

# სიაში შემთხვევაში:
my_list = [1, 2, 3, 4, 5]
print("სიის საშუალო არითმეტიკული:", average_of_list(my_list))

4. #სიების შეერთება:

def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

# ორი სია:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("ორი სიის შეერთება:", merge_lists(list1, list2))

5. #დუბლიკატების სია:

def remove_duplicates(lst):
    return list(set(lst))

# სია:
my_list = [1, 2, 2, 3, 4, 4, 5]
print("სიის დუბლიკატების წაშლა:", remove_duplicates(my_list))











