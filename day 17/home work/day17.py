# თამაშების ლისტის შექმნა
games = ["gamez", "Sololern", "w3", "codewars", "ez"]
replacements = {
    "gamez": "Sololern",
    "w3": "Sololern",
    "codewars": "ez"
}

for i in range(len(games)):
    if games[i] in replacements:
        games[i] = replacements[games[i]]

print(games)

