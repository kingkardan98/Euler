from tqdm import tqdm

# This is an extremely inefficient implementation, but I had some time to waste at work so here goes.
# This took 20 minutes to execute, but whatever
LIMIT = 1_000_000_000


def is_strongly_even(num):
    # This condition kills off a lot of numbers that automatically doesn't qualify.
    for digit in str(num):
        if int(digit) % 2 == 1:
            return False
    return True


def is_strongly_odd(num):
    # While this is a bit less intuitive, a strongly odd number, when reversed and added,
    # will always yield an even number.
    for digit in str(num):
        if int(digit) % 2 == 0:
            return False
    return True


def reverse(num):
    return int(str(num)[::-1])


def main():
    seen = set()
    reversibles = set()
    for number in tqdm(range(LIMIT), desc="Checking numbers"):
        if number in seen:
            # I've already checked it's reverse, skip it
            continue

        rev = reverse(number)
        if len(str(rev)) != len(str(number)):
            # If the reverse has leading zeros, skip it
            continue

        if is_strongly_odd(number) or is_strongly_even(number):
            continue
        if rev % 2 == number % 2:
            continue
        if not is_strongly_odd(number + rev):
            continue

        if True:
            reversibles.add(number)
            reversibles.add(rev)
        seen.add(number)
        seen.add(rev)
    print(len(reversibles))


main()
