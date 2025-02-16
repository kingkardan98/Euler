from recurring_functions.Totatives import coprime_set
from tqdm import tqdm

max = 12000
frac_counter = 0
tracker = tqdm(total=max)

# Loop through the denominators
for d in range(2, max + 1):
    fractions = [(i, d) for i in coprime_set(d)]  # Generate coprime pairs
    for fraction in fractions:
        value = fraction[0] / fraction[1]  # Calculate the fraction value
        if 1/3 < value < 1/2:  # Check if it's between 1/3 and 1/2
            frac_counter += 1
    tracker.update(1)

tracker.close()
print(frac_counter)
