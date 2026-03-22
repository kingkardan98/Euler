import math, time
from tqdm import tqdm

def compare_large_exponents(x,y,z,w):
    if y * math.log(x,math.e) > w * math.log(z,math.e):
        return x, y
    else:
        return z, w

def main():
    with open("problem_99.txt","r") as f:
        text = f.readlines()
    powers = [tuple(map(int, line.strip().split(","))) for line in text]

    champion = (1, 1)
    highest = 0

    pbar = tqdm(total=len(powers), desc="Comparing")

    start = time.time()
    for i in range(len(powers)):
        new_champion = compare_large_exponents(*champion, *powers[i])

        if new_champion != champion:
            champion = new_champion
            highest = i + 1 # Project Euler is 1-indexed!
        pbar.update(1)

    end = time.time()
    time.sleep(0.1)

    print("Highest index:", highest)
    print("Time taken:", end - start)
    print("Time for iteration:", (end - start) / 1000)

main()