import re
from itertools import product, permutations
from fractions import Fraction
from typing import List, Set

NUMBER_OR_OP = re.compile(r'^[0-9\(\)\+\-\*\/ ]+$')

def safe_eval_fraction(expr: str) -> Fraction:
    """Evaluate expr using Fraction arithmetic. Assumes only digits, + - * / and parentheses."""
    if not NUMBER_OR_OP.match(expr):
        raise ValueError("Expression contains unexpected characters")
    # replace integer literals with Fraction(...)
    expr_with_fracs = re.sub(r'\d+', lambda m: f"Fraction({m.group(0)})", expr)
    return eval(expr_with_fracs, {"Fraction": Fraction})

# -----------------------
# Expression generation
# -----------------------

OPS = ['+', '-', '*', '/']

def combine_results(left: List[str], right: List[str], op: str) -> List[str]:
    """Return strings combining each left expr with each right expr using op, with parentheses."""
    out = []
    for le in left:
        for re in right:
            out.append(f"({le}{op}{re})")
    return out

def all_parenthesized_expressions_for_ops(nums: List[int], ops: List[str]) -> Set[str]:
    """
    Given operand list nums (length n) and ops list (length n-1),
    return all fully parenthesized expressions (as strings) that respect operand order
    and the operator choices.
    """
    n = len(nums)
    assert n >= 1
    if n == 1:
        return {str(nums[0])}
    results = set()
    # split between every possible left/right partition
    # left gets k operands, right gets n-k operands, join operator is ops[k-1]
    for k in range(1, n):
        left_nums = nums[:k]
        right_nums = nums[k:]
        left_ops = ops[:k-1]        # operators internal to left block
        right_ops = ops[k:]         # operators internal to right block
        left_exprs = all_parenthesized_expressions_for_ops(left_nums, left_ops) if len(left_nums) > 1 else {str(left_nums[0])}
        right_exprs = all_parenthesized_expressions_for_ops(right_nums, right_ops) if len(right_nums) > 1 else {str(right_nums[0])}
        join_op = ops[k-1]
        # combine all left x right using join_op
        for le in left_exprs:
            for re in right_exprs:
                results.add(f"({le}{join_op}{re})")
    return results

def expressions_for_fixed_order(nums: List[int]) -> Set[str]:
    """
    For a fixed ordering of nums, generate all operator choices and parenthesizations.
    Returns set of expression strings (parentheses included).
    """
    n = len(nums)
    if n == 1:
        return {str(nums[0])}
    results = set()
    for ops_choice in product(OPS, repeat=n-1):
        exprs = all_parenthesized_expressions_for_ops(nums, list(ops_choice))
        # remove redundant outer parentheses for nicer eval strings, but not required
        # keep them for safety / clarity
        results.update(exprs)
    return results

def createExpressions(a: int, b: int, c: int, d: int) -> Set[str]:
    """
    Generate ALL expressions for the four operands, including all permutations of operands,
    all operator choices, and all parenthesizations.
    Returns a set of expression strings.
    """
    results: Set[str] = set()
    operands = [a, b, c, d]
    for perm in set(permutations(operands)):
        results.update(expressions_for_fixed_order(list(perm)))
    return results

def checkExpressions(a: int, b: int, c: int, d: int, bracketMap=None) -> Set[str]:
    """
    Compatibility wrapper to keep your main() unchanged: previously this took a bracketMap,
    now it's unused; checkExpressions returns the full set of bracketed expressions.
    """
    return createExpressions(a, b, c, d)

# -----------------------
# keep your helper for consecutive detection unchanged (but ensure correct filtering)
# -----------------------

def findConsecutives(results: set) -> int:
    """Return the length of the consecutive run of positive integers starting from 1."""
    if not results:
        return 0
    # keep only positive integers (Fractions with denominator 1 and >=1)
    ints = {int(x) for x in results if getattr(x, 'denominator', 1) == 1 and x >= 1}
    n = 1
    count = 0
    while n in ints:
        count += 1
        n += 1
    return count

# -----------------------
# Main (unchanged semantics)
# -----------------------

def main():
    # bracketMap parameter is no longer needed but left for compatibility
    bracketMap = None
    max_n = 0
    best_tuple = None

    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    operations = checkExpressions(a, b, c, d, bracketMap)
                    results = set()
                    for op in operations:
                        try:
                            val = safe_eval_fraction(op)
                        except (ZeroDivisionError, OverflowError, ValueError):
                            continue
                        except Exception:
                            continue
                        results.add(val)
                    consecutives = findConsecutives(results)
                    if consecutives > max_n:
                        max_n = consecutives
                        best_tuple = (a, b, c, d)
                        print(f"New best: {max_n} consecutive integers starting at 1 from {a} {b} {c} {d}")
    print("Done. Best:", max_n, "from", best_tuple)
    return

if __name__ == "__main__":
    main()
