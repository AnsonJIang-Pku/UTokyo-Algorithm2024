# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/177661
def shakersort(array):
    left, right = 0, len(array) - 1
    swapped = 0 # 最后发生交换的位置
    num = 0 # 走查的回数
    while left < right:
        num += 1
        for i in range(left, right):
            if array[i+1] < array[i]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = i
        right = swapped
        for j in range(right, left, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swapped = j
        left = swapped
    return array, num

N = int(input())
array = list(map(int, input().split()))
sorted_arr, k = shakersort(array)
print(k)
for i in range(N):
    print(sorted_arr[i], end = ' ')
