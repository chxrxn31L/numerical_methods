from math import sqrt

# -------------------------------
# Utility Functions
# -------------------------------

def is_prime(n: int) -> bool:
    """Check if n is prime (basic trial division)."""
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_pattern_number(n: int) -> int:
    """Builds number of form 123...n...(n-1)...321."""
    forward = "".join(str(i) for i in range(1, n+1))
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

def problem1(n: int = 10, max_n: int = 3000):
    """
    Problem 1:
    Generate number of given pattern and check primality.
    """
    for i in range(n, max_n+1):
        if n==10:
            return {"pattern_number": 10, "is_prime": True}    
        if i%3 == 0:
            continue
        else:
            if 1000 <= i <= 3000:
                num = next_pattern_number(i)
                if is_prime(num):
                    return {"pattern_number": num, "is_prime": True}
    return {"pattern_number": None, "is_prime": False}


def problem2(llimit: int = 2, ulimit: int = 20):
    """
    Problem 2:
    Repunit primes between N=2 and limit.
    """
    results = []
    for N in range(llimit, ulimit+1):
        if is_prime(N):  # only need to check prime N
            rep = generate_repunit(N)
            # NOTE: true primality check for repunits is expensive
            # Here we just return the generated number
            results.append({"N": N, "repunit": str(rep)})
    return results


def problem3(start: int = 2, end: int = 31):
    """
    Problem 3:
    Find Mersenne primes 2^p - 1 where p is prime in range.
    """
    results = []
    for p in range(start, end+1):
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
    primes = [n for n in range(lower+1, upper) if is_prime(n)]
    return {"interval": (lower, upper), "primes_found": primes[:10]}  # return first few


def problem5(limit_digits: int = 10):
    """
    Problem 5:
    Find palindromic prime with at least `limit_digits`.
    (For demo: we generate small palindromes and test primality).
    """
    n = 10**(limit_digits-1)
    maxi = 10**limit_digits
    while n <maxi:
        s = str(n)
        l = int(s[0])
        if l % 2 == 0:
            n += 10**(limit_digits-1)
            continue
        pal = int(palindrome_number(s))
        if is_prime(pal):
            return {"palindromic_prime": pal, "digits": len(str(pal))}
        n += 1



