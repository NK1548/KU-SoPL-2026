# Student ID : 52552
# Course     : Survey of Programming Languages — KU-SoPL-2026
#
# ╔══════════════════════════════════════════════════════════╗
# ║  YOUR TASK                                               ║
# ║                                                          ║
# ║  Return the absolute difference between the sum of even digits and the sum of odd digits.║
# ║                                                          ║
# ║  - digits are extracted from your ID string              ║
# ║  - ignore the "-ex" suffix if present                    ║
# ╚══════════════════════════════════════════════════════════╝
#
# Implement solve() below and return an integer.
# Do NOT rename this file.
# Run with:  python task_52552.py


def solve(id: str) -> int:
    
    digits = [int(c) for c in id if c.isdigit()]
    even_sum = sum(d for d in digits if d % 2 == 0)
    odd_sum = sum(d for d in digits if d % 2 != 0)
    return abs(even_sum - odd_sum)

if __name__ == "__main__":
    print(solve("52552"))
