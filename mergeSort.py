

# 배우고 부족했던 것 : 시점 개념 호출 개념
import numpy as np

if __name__ == '__main__':



    def merge_sort(left, right, merge_list):


        # 파이썬 //는 소수점을 버린다

        # 호출 개념좀 . 험수 호출 개념 미약하니 어떻게 타고 들어가는 지 모른다 타고 들어가서 헤맨다
        # 기본이 너무 부족
        # 메인에서 merge_sort 호출 -> merge_sort 함수 내부에서 재귀(자기자신) 호출
        # void 함수 개념도, 직접 값으로 return 하지는 않지만 처리만 해준다

        # 1단위까지 쪼갰을 때 left = 0 ,middle은 if문 내부에서 0이 되고 , right는 1로 들어왔을 것이다
        # 이 if문으로 설정하면 왼쪽 오른 쪽 양 쪽 모두 재귀호출 되면 안될 때 재귀호출 되지 않는다.
        if left < right:
            # 재귀 호출 인덱스 추상화 리스트 추상화 left가 right(middle) 값은 parameter 가 들어온다면 더 이상 호출하지 않는다
            # 그러므로 left가 0이고 right가 1 일때의 '시점'에서는 밑의 merge_sort 함수가 호출되지 않을 것이고 merge로 들어간다 -> merge되고 나서 호출된 부분으로 돌아간다 -> 여기서는 left와 right가 각각 0과 1로 들어온 시점 0,3 index에서 호출
            # 0~3 시점에서 left conquer가 끝난것이니 right conquer로 넘어간다 . 두 계단 올라가는 것임

            middle = (left + right) // 2
            merge_sort(left, middle, merge_list)
            # 리스트가 1단위 까지 쪼개졌을 때(index가) middle이 0 (소수점을 버리므로) right가 1이므로 더 이상 호출하지 않도록 middle+1을 해준다
            merge_sort(middle+1, right, merge_list)
            merge(left, middle,right, merge_list)


    # 리스트를 자르면 자원을 많이 사용하므로 바꾸는 게 좋다
    # middle과 right는 엄연히 다르게 쓰인다 left의 right가 아니라 right는 가장 끝의 개념으로 쓰인다 재귀호출 할때와 쓰임이 다름 .
    # 재귀 호출 할 때만 middle이 argument로 넘어가 나뉘어진 리스트의 right  parameter 로 받는 것 뿐

    def merge(left,middle,right,merge_list):
        # 본래의 리스트로 복사하기 위함

        i = left
        j = middle+1
        # sorted_list 의 변수
        k = left

        sorted = list(np.random.randint(100 , size = len(list_)))

        while i <= middle and j <= right:
            if merge_list[i] <= merge_list[j]:
                sorted[k] = merge_list[i]
                k += 1
                i += 1

            else:
                sorted[k] = merge_list[j]
                k+=1
                j+= 1

        if i > middle:
            for l in range(j, right+1):
                sorted[k] = merge_list[l]
                k += 1

        else:
            for q in range(i, middle+1):
                sorted[k] = merge_list[q]
                k+=1

        for l in range(left , right+1):
            merge_list[l] = sorted[l]

    # 메인 호출 (입력) 프로그래밍 기본개념에 충실할 것 , 입력 - > 처리(함수) -> 출력
    list_ = [8, 9, 10,3 ,5, 6 ]

    print(merge_sort(0, len(list_)-1, list_))

    for i in range(len(list_)):
        print(list_[i])

    # 개념으로 짜도 디버깅이 안되네 디버깅은 타고 들어가는 게 맞다 어느 시점에 어떻게 들어가고 있는 건지 알아야 되는 거고 개념을 알고 가야 할 수 있다 개념 모르면 어느 시점인지 뭔지 모른다 변수가 뭘 의미하는 지 개념 기초의 목적도 개념이고 문제 풀이의 목적도 개념이다