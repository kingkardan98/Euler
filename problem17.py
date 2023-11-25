import inflect

eng = inflect.engine()
charSum = 0

for i in range(1, 1001):
    numWord = eng.number_to_words(i)
    for char in numWord:
        if char.isalpha():
            charSum += 1

print(charSum)