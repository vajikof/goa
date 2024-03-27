#2) ფილმების სია:
favorite_movies = ["შენი სახლი", "მიწიერი ადამიანი", "ჰერული"]
print(favorite_movies)



#3) შექმენით სტრინგი:
name = "ანდრიანი"
first_char = name[0]
last_char = name[-1]
print(first_char, last_char)

#4) შექმენით სია და სტრინგი და დაბეჭდეთ len ფუნქციის გამოყენებით მათი ზომა:

sample_list = [3, 6, 9, 12, 15]
sample_string = "OpenAI"
print(len(sample_list), len(sample_string))


#5) შეცვალეთ სიიდან რომელიმე მწიშვნელობა:

sample_list[2] = 18
print(sample_list)


#6) შექმენით რიცხვების სია სადაც 10 რიცხვს შეიტანთ, და დაბეჭდეთ პირველი და ბოლო ინდექსზე მყოფი ელემენტების ჯამი:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = numbers[0] + numbers[-1]
print(total)
