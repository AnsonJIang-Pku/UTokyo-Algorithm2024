# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/177662
# 只进行第一次的快速排序
def qsort_once(array, left, right):
    pivot = array[right]
    j = left # cursor B，移动目标位置
    for i in range(left, right): # cursor A 扫描指针
        if array[i] <= pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    # 此时i (cursor A) 到达pivot元素，交换pivot和j所指元素
    array[right], array[j] = array[j], array[right]

# 完整的快速排序
def qsort(array, left, right):
    if left >= right:
        return
    pivot = array[right]
    j = left # cursor B，移动目标位置
    for i in range(left, right): # cursor A 扫描指针
        if array[i] <= pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    # 此时i (cursor A) 到达pivot元素，交换pivot和j所指元素
    array[right], array[j] = array[j], array[right]
    # Recursion
    qsort(array, left, j-1)
    qsort(array, j+1, right)

def output(array):
    for i in range(len(array)):
        print(array[i], end = ' ')
    print()

N = int(input())
array = list(map(int, input().split()))
qsort_once(array, 0, N-1)
output(array)
qsort(array, 0, N-1)
output(array)
