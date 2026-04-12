LIMIT = 10**6
TEST = 12


def generate_divsums(limit):
    sum_arr = [0 for _ in range(limit+1)]

    for i in range(1, limit + 1):
        for j in range(i*2, limit + 1, i):
            sum_arr[j] += i

    return sum_arr


def chain_builder(sum_arr):
    chains = []
    seen = set()

    for i in range(len(sum_arr)):
        if i in seen:
            continue

        new_i = i
        chain = []

        while True:
            if new_i in chain:
                # cycle detected
                cycle_start = chain.index(new_i)
                chains.append(chain[cycle_start:])
                break

            if new_i >= len(sum_arr):
                break

            chain.append(new_i)
            seen.add(new_i)
            new_i = sum_arr[new_i]

    return set(tuple(sorted(chain)) for chain in chains if chain != [0])


def main():
    sums = generate_divsums(LIMIT)
    amicable_chains = chain_builder(sums)

    champion = tuple()
    for chain in amicable_chains:
        if len(chain) > len(champion):
            champion = chain

    print(min(champion))


if __name__ == '__main__':
    main()