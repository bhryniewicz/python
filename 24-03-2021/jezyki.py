
languages = ["Python", "C#", "JS", "PHP", "Java"]

print(type(languages))

print(f"Pierwszy: {languages[0]}\nOstatni: {languages[len(languages) - 1]}")

languages.append("React")
print(languages)

print(languages.count("Python"))

for language in range(3):
    languages.append("Python")

print(languages.count("Python"))

languagesAgain = ["C++", "JavaScript"]

languages.extend(languagesAgain)
print(languages)

languages = list(dict.fromkeys(languages))
print(languages)

