import sys
from math import sqrt

path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
 
T = int(input())
min_penalty = sys.maxsize
 




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

def find_least_penalty_and_order(nums):
    nums.sort()
    lower = min(nums) - 2 * len(nums)
    upper = max(nums) + 2 * len(nums)
    primes = find_primes(lower, upper)
    
    min_penalty = float('inf')
    min_primes = None

    for i in range(len(primes) - len(nums)):
        consecutive_primes = primes[i:i+len(nums)]
        penalty = sum([abs(a - b) for a, b in zip(consecutive_primes, nums)])

        if penalty < min_penalty:
            min_penalty = penalty
            min_primes = consecutive_primes

    return min_penalty, min_primes


import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
 
T = int(input())
min_penalty = sys.maxsize
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print(n,nums)
    min_penalty, ordered_primes = find_least_penalty_and_order(nums)
    print("The least penalty for making consecutive primes: ", min_penalty)
    print("Nearest sorted consecutive primes: ", ordered_primes)



        #     prime_list = generate_prime_list(num, n)
        #     print(prime_list)
        # elif not is_prime(num):
        #     start_prime = find_nearest_prime(num)
        #     prime_list = generate_prime_list(start_prime, n)
        #     print(prime_list)




# 연속한 소수리스트를 먼저 만들지 말고
# 각 값에서 가장 가까운 소수를 만들고 최소 최대를 찾은 다음에 
# 연속시킨다
# 최소 최대가 있으니까 
# 페널티가 늘어나면 중단시키는방법 

# for _ in range(T):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     print(n,nums)
#     for num in nums:
#         print(find_nearest_prime(num))
#     # print(n,nums)

# min_penalty = float('inf')
# result = None
# def is_consecutive(primes): # 하나씩 연속하게 만들기

#     for i in range(len(primes) - 1):
#         if primes[i] + 2 != primes[i+1]:
#             return False
#     return True


# for ordered_nums in permutations(nums, len(nums)):
#     for prime_combination in possible_prime_combinations:
#         penalties = [abs(prime - num) for prime, num in zip(prime_combination, ordered_nums)]
#         total_penalty = sum(penalties)

#         if total_penalty < min_penalty:
#             min_penalty = total_penalty
#             result = ordered_nums


# 연속된 소수배열을 이동시키면 되겠다 다 만들고 그 특정 소수배열을 찾으려하기보다
# 
# 최솟값을 없애고 마지막껄 늘리면서, 그러면서 최쇳값찾으면되겟네 
