from tqdm import tqdm
from recurring_functions.Totatives import phi

def main():
    limit = 1000000
    max_n = 0
    max_f = 0
    tracker = tqdm(total=limit)
    for n in range(2, limit + 1):
        fraction = n / phi(n)
        if fraction > max_f:
            max_f = fraction
            max_n = n
        tracker.update(1)
    tracker.close()
    print(max_n)

if __name__ == '__main__':
    main()