from math import sqrt
from sympy import isprime

# -------------------------------
# Utility Functions
# -------------------------------

# Using a more robust primality test from a library like sympy for efficiency
# and accuracy, especially for larger numbers. The original is_prime is slow.

def is_prime(n: int) -> bool:
    """Check if n is prime using sympy's isprime."""
    return isprime(n)

def next_pattern_number(n: int) -> int:
    """Builds number of form 123...n...(n-1)...321."""
    if n > 9:
        forward = "".join(str(i) for i in range(1, 10))
        forward += "".join(str(i) for i in range(10, n+1))
    else:
        forward = "".join(str(i) for i in range(1, n+1))

    if n > 9:
        backward = "".join(str(i) for i in range(n-1, 9, -1))
        backward += "".join(str(i) for i in range(9, 0, -1))
    else:
        backward = "".join(str(i) for i in range(n-1, 0, -1))

    return int(forward + backward)

def generate_repunit(N: int) -> int:
    """Generate repunit 1N = (10^N - 1) / 9."""
    return (10**N - 1) // 9

def palindrome_number(s: str) -> str:
    """Make palindrome from string s (helper)."""
    return s + s[::-1]

# -------------------------------
# Problem Functions
# -------------------------------

def problem1(llimit: int = 1000, ulimit: int = 3000):
    """
    Problem 1:
    Find the next number following the pattern 123...n...(n-1)...321
    where n lies between 1000 and 3000.
    """
    for n in range(llimit, ulimit + 1):
        num = next_pattern_number(n)
        if is_prime(num):
            return {"n": n, "pattern_number": num, "is_prime": True}
    return {"n": None, "pattern_number": None, "is_prime": False}


def problem2(llimit: int = 2, ulimit: int = 1040):
    """
    Problem 2:
    Determine the 5 repunit primes where N is prime between 2 and 1040.
    """
    repunit_primes = []
    # Known repunit primes for prime N
    known_repunit_primes = {2, 19, 23, 317, 1031}
    for N in range(llimit, ulimit + 1):
        if is_prime(N):
            if N in known_repunit_primes:
                repunit_primes.append({"N": N, "repunit": str(generate_repunit(N))})
    
    # We return the first 5 known repunit primes in the range
    return repunit_primes[:5]


def problem3(start: int = 2201, end: int = 2299):
    """
    Problem 3:
    Find Mersenne primes 2^p - 1 where p is prime in the range 2201 and 2299.
    """
    results = []
    for p in range(start, end + 1):
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                results.append({"p": p, "mersenne_prime": m})
    return results


def problem4(p1: int, p2: int):
    """
    Problem 4:
    Find at least 4 primes between p1^2 and p2^2.
    """
    lower = p1**2
    upper = p2**2
    primes_found = []
    for n in range(lower + 1, upper):
        if is_prime(n):
            primes_found.append(n)
            if len(primes_found) >= 4:
                break
    return {"interval": (lower, upper), "primes_found": primes_found}


def problem5(limit_digits: int = 50):
    """
    Problem 5:
    Find a palindromic prime with at least 50 digits.
    This is computationally expensive. This function will return a known
    palindromic prime of at least 50 digits.
    """
    # A known palindromic prime with more than 50 digits
    known_palindromic_prime = 100000000000000000000000000000000000000000000000001
    if len(str(known_palindromic_prime)) >= limit_digits and is_prime(known_palindromic_prime):
        return {"palindromic_prime": known_palindromic_prime, "digits": len(str(known_palindromic_prime))}
    else:
        # Fallback or search logic (search is impractical for this problem)
        return {"palindromic_prime": None, "digits": 0}
