#პირველ დავალებისთვის, გავაკეთო რანჯის კოპიო ფუნქციის შექმნა:

def my_range(start, end, step):
    result = []
    current = start
    while current < end:
        result.append(current)
        current += step
    return result

#დავალება 2-ისთვის, შევქმნათ my_filter ფუნქცია:

def my_filter(lst, symbol):
    return [item for item in lst if item != symbol]


#დავალება 3-ისთვის, შევქმნათ სიის ყველა ელემენტის გამრავლების ფუნქცია:

def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result


#დავალება 4
def greet(username):
    print("Welcome", username, "here!")

#დავალება 5
def sum_of_odd_numbers(lst):
    andd_sum = 0
    for num in lst:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum












