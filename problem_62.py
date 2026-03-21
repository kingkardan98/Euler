from collections import defaultdict

def find_smallest_cube_with_five_permutations():
    """
    Find the smallest cube for which exactly five permutations of its digits are also cubes.
    """
    cubes = defaultdict(list)  # Map sorted digit signature to a list of cubes

    n = 1
    while True:
        cube = n ** 3
        # Generate the digit signature by sorting the digits of the cube
        signature = ''.join(sorted(str(cube)))
        cubes[signature].append(cube)

        # Check if any signature has exactly five cubes
        if len(cubes[signature]) == 5:
            return min(cubes[signature])  # Return the smallest cube in the group

        n += 1

if __name__ == "__main__":
    result = find_smallest_cube_with_five_permutations()
    print("The smallest cube with exactly five permutations that are cubes is:", result)
