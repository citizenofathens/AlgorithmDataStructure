from itertools import permutations
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def find_primes(lower, upper):
    primes = []
    for i in range(lower, upper + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def find_consecutive_primes(length):
    consecutive_primes = []
    prime_candidate = 2
    
    while len(consecutive_primes) < length:
        if is_prime(prime_candidate):
            if not consecutive_primes or prime_candidate - consecutive_primes[-1] == 2:
                consecutive_primes.append(prime_candidate)
            else:
                consecutive_primes = [prime_candidate]
        prime_candidate += 1

    return consecutive_primes

def find_least_penalty_and_order(nums):
    min_penalty = float('inf')
    best_order = None
    consecutive_primes = find_consecutive_primes(len(nums))
    
    for ordered_nums in permutations(nums):
        penalty = sum(abs(consecutive_primes[i] - ordered_nums[i]) for i in range(len(nums)))
        
        if penalty < min_penalty:
            min_penalty = penalty
            best_order = ordered_nums

    return min_penalty, best_order

if __name__ == "__main__":
    nums = [7, 13, 3]
    min_penalty, best_order = find_least_penalty_and_order(nums)
    print("The least penalty for making consecutive primes: ", min_penalty)
    print("The best order for consecutive primes: ", best_order)
