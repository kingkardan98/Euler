results = []

for a in range(2, 101):
    for b in range(2, 101):
        if not (a**b in results):
            results.append(a**b)

print(len(results))