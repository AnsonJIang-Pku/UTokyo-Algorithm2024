# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/176778
def binary_search(array, v, N):
    left, right = 0, N - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] <= v:
            left = mid + 1
        else:
            right = mid - 1
            if array[right] <= v: //否则可能丢掉正确的值
                break
    return mid

N = int(input())
array = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    v = int(input())
    if v >= array[N-1]:
        print("not exist")
        continue
    mid = binary_search(array, v, N)
    print(array[mid])

    
