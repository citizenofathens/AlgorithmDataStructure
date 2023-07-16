import sys
path = '21395.txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
 
T = int(input())
min_penalty = sys.maxsize

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nearest_prime(y):
    i = 0
    while not is_prime(y + i) and not is_prime(y - i):
        i += 1
    return y + i if is_prime(y + i) else y - i


def generate_prime_list(start_prime, num_len):
    return_list = []
    while len(return_list) != num_len:
        start_prime += 1 
        if is_prime(start_prime):
            return_list.append(start_prime)
        else:
            pass
    return return_list

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print(n,nums)
    # print(n,nums)
    for num in nums:
        if is_prime(num):
            start_prime = num
            prime_list = generate_prime_list(start_prime, n)
            print(prime_list)
        elif not is_prime(num):
            start_prime = find_nearest_prime(num)
            prime_list = generate_prime_list(start_prime, n)
            print(prime_list)
 