# 내림 차순 구현
def bubble_sort(target_list, length):
    for i in range(length - 1, -1, -1):
        for j in range(0, i, 1):
            if (target_list[j] < target_list[j + 1]):
                temp = target_list[j]
                target_list[j] = target_list[j + 1]
                target_list[j + 1] = temp
    return target_list


# 오름차순 구현
def bubbleSort(list_):
    for i in range(len(list_)):
        for j in range(i + 1, len(list_)):
            # list_[i] 는 모든 list_[j] 와 비교하므로 가장 작은 list_[j] 값이 담긴다.
            if list_[i] > list_[j]:
                temp = list_[i]
                list_[i] = list_[j]
                # x 할당 개념 할당했으면 바뀐 건데 그걸 다시 넣으면 안 된다
                # list_[j] = list_[i]
                list_[j] = temp
            print(list_)
    return list_