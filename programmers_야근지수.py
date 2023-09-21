
import math
import copy

def solution(n, works):
    # 야근 피로도 : 야근 시작 시점에서 남은 일의 작업량을 제곱하여 더한다
    if len(works) ==0:
        return 0
    answer = 0
    count_n = copy.copy(n)
    works.sort(reverse=True)
    for idx in range(len(works)+1):
        if idx == len(works):
            idx = idx//n

        if works[idx] ==0:
            pass
        else:
            works[idx] -= 1
        count_n -=1

        if count_n ==0:
            answer =  int(sum(list(map(lambda x: math.pow(x,2), works))))
            return answer
        # 큰 값부터 처리한 뒤 1번 줄여도 다른 값보다 크다면 다시 큰값부터

    return answer