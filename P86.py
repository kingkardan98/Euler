import math
from math import gcd, isqrt

def count_for_M(M, target=None):
    total = 0
    max_s = 2 * M
    max_c = M

    # generate primitive Pythagorean triples via Euclid's formula
    # we need u up to sqrt(max_s + max_c) roughly -- using sqrt(2*M) is safe and small
    u_limit = int(math.sqrt(max_s + max_c)) + 2

    seen_pairs = set()  # avoid double processing same (s,c) from different primitives

    for u in range(2, u_limit):
        for v in range(1, u):
            if (u - v) % 2 == 0:  # same parity -> skip
                continue
            if gcd(u, v) != 1:
                continue
            a = u*u - v*v   # leg1
            b = 2*u*v       # leg2

            # consider multiples of the primitive triple
            k = 1
            while True:
                leg1 = k * a
                leg2 = k * b

                # try both assignments: (s, c) = (leg1, leg2) and (leg2, leg1)
                for s_candidate, c_candidate in ((leg1, leg2), (leg2, leg1)):
                    if s_candidate > max_s or c_candidate > max_c:
                        continue
                    pair = (s_candidate, c_candidate)
                    if pair in seen_pairs:
                        continue
                    seen_pairs.add(pair)

                    # count number of (x,y) with x<=y<=c and x+y = s
                    a_min = max(1, s_candidate - c_candidate)
                    a_max = s_candidate // 2
                    cnt = max(0, a_max - a_min + 1)
                    total += cnt

                    if target is not None and total >= target:
                        return total

                # stop if both legs already exceed both bounds (so further k will only increase)
                if min(leg1, leg2) > max_s and min(leg1, leg2) > max_c:
                    break
                # break if both scaled legs are larger than our largest needed limits
                if leg1 > max_s and leg1 > max_c and leg2 > max_s and leg2 > max_c:
                    break
                k += 1

    return total

count = 0
m = 1
while count < 1*10**6:
    count = count_for_M(m)
    print("{}: {}".format(m, count))
    m += 1
