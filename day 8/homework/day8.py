required_weight = 50
required_height = 170

weight = int(input("your weight: "))
height = int(input("your height: "))

if weight == required_weight and height == required_height:
    print("sworia")

elif weight > required_weight and height < required_height:
    print("soso")

elif weight < required_weight and height > required_height:
    print("sworia")

elif weight == required_weight:
    print("sworia")

elif height == required_height:
    print("sworia")

else:
    print("arasworia")


# შედარების ოპერატორები -    .    <, >, ==, >=, <=, !=
# მათემატიკური ოპერატორები -   . -, +, *, / ,