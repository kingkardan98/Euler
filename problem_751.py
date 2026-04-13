from math import floor
from decimal import Decimal, getcontext

getcontext().prec = 50  # Set precision higher than you need

THETA = Decimal('2.3581321345589146')
TAU = Decimal('2.9')

def b(n):
    sequence = [THETA]
    for i in range(1, n):
        prev = sequence[i - 1]
        new_member = int(prev) * (prev - int(prev) + 1)
        sequence.append(new_member)
    return sequence

def a(n):
    return int(b(n)[-1])

def concatenate(a_seq):
    decimal_part_list = [str(num) for num in a_seq[1:]]
    decimal_part = ''.join(decimal_part_list)
    return Decimal(str(a_seq[0]) + '.' + decimal_part)

def avg(a, b):
    return (a + b) / 2


while abs(THETA - TAU) > Decimal('1e-30'):
    THETA = TAU
    seq = []
    for num in range(1, 45):
        seq.append(a(num))
    TAU = concatenate(seq)

    print(f"THETA: {round(THETA, 24)}")
    print(f"TAU:   {round(TAU, 24)}")
    print(f"diff:  {THETA - TAU}")

