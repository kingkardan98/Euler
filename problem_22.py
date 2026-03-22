def calculate_name_score(name):
    total = 0
    for char in name.lower():
        # Since the Unicode of 'a' is 97, subtract 96
        total += ord(char) - 96
    return total


with open('P22_aux.txt', 'r') as file:
    for line in file:
        raw_names = line.split(',')

# Remove double quotes from names
cleaned_names = []
for raw_name in raw_names:
    cleaned_name = raw_name.replace('"', '')
    cleaned_names.append(cleaned_name)

# Sort names alphabetically
cleaned_names.sort()

# Calculate total score
total_score = 0
for index in range(len(cleaned_names)):
    total_score += calculate_name_score(cleaned_names[index]) * (index + 1)

print(total_score)