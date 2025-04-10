
# 재귀 함수로 구현하는 바이너리 탐색 코드
def binary_search(array, target, start , end):
    if start > end:
        return None

    for a in array:
        if a == target:
            return a

    #end = start //2
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start,mid -1)
    else:
        return binary_search(array,target,mid+1,end)


# 반복문으로 구현하는 이진탐색 코드

def binary_search(array, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))

array = list(map(int,input().split()))



# 부품 찾기

# 확인해야할 부품번호


import sys

# 데이터 많은 경우 sys 사용
input_data = sys.stdin.readline().rstrip()

N = list(map(int,input().split()))[0]
numbers = list(map(int,input().split()))
M = list(map(int,input().split()))[0]
targets = list(map(int,input().split()))[0]


numbers.sort()

def binary_search(array, target, start, end,answers):
    if start >= end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return 'yes'
    elif array[mid] >= target:
        binary_search(array,target, start, mid-1)
    else:
        binary_search(array,target,mid+1,end)




answers = []

for target in targets:
    is_in = binary_search(answers)
    answers.append(is_in)







