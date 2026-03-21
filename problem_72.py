from tqdm import tqdm
from recurring_functions.Totatives import phi

max = 1000000
counter = 0

tracker = tqdm(total=max)

for d in range(2, max+1): # We start at 2, there's no use in starting at 1
    counter += phi(d)
    tracker.update(1)

tracker.close()
print(counter)
