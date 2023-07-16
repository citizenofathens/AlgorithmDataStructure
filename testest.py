import sys
from math import sqrt

def sieve_of_eratosthenes_in_range(lower, upper):
    full_sieve = [True] * (upper + 1)
    full_sieve[0] = full_sieve[1] = False
    
    for i in range(2, int(sqrt(upper)) + 1):
        if full_sieve[i]:
            for j in range(i * i, upper + 1, i):
                full_sieve[j] = False
    
    primes_in_range = [i for i in range(lower, upper + 1) if full_sieve[i]]
    return primes_in_range

def find_least_penalty_and_order(nums):
    nums.sort()
    lower = nums[0] - 2 * len(nums)
    upper = nums[-1] + 2 * len(nums)
    primes = sieve_of_eratosthenes_in_range(lower, upper)
    
    min_penalty = float('inf')
    min_primes = None

    for i in range(len(primes) - len(nums) + 1):
        consecutive_primes = primes[i:i+len(nums)]
        penalty = sum([abs(a - b) for a, b in zip(consecutive_primes, nums)])
        
        if penalty < min_penalty:
            min_penalty = penalty
            min_primes = consecutive_primes
            
            if min_penalty == 0:
                break

    return min_penalty, min_primes

path = '21395.txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
import time
T = int(input())
min_penalty = sys.maxsize
start_time = time.time()
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split())) 
    min_penalty, ordered_primes = find_least_penalty_and_order(nums)
    print( min_penalty) 
    
print(time.time()-start_time )