from tqdm import tqdm
from recurring_functions.Totatives import phi

M = 1000000
counter = 0

tracker = tqdm(total=M)

for d in range(2, M + 1): # We start at 2, there's no use in starting at 1
    counter += phi(d)
    tracker.update(1)

tracker.close()
print(counter)
