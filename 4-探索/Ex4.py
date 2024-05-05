# source: https://eeic-algorithms.train.tracks.run/train/10750/challenge/176779
# 连续子列一般涉及到双指针法
# 返回数组中满足子序列和大于等于target的子列个数
def num_subarray(array, target):
    count = 0
    sum = 0
    j = 0 #用双指针可避免每次重复求和，时间复杂度O(N)
    for i in range(len(array)):
        #由于元素均为正数, 只要找到第一个>=target的数组, 那么直到末尾都满足条件
        while j < len(array) and sum < target:
            sum += array[j]
            j += 1
        if sum >= target:
            count += len(array) - j + 1
        #现在[i,j]子列的和>=target,因此需要后移i减小子列和
        sum -= array[i]
    return count

# 知道了查找范围，利用二分法查找满足条件的子列个数
# 数组中的连续子列和>=target的刚好有K个
def binary_search(array, K):
    left, right = min(array), sum(array)
    while left <= right:
        mid = (left + right) // 2
        num = num_subarray(array, mid)
        if num <= K:
            right = mid - 1
        else:
            left = mid + 1
    return right
    #关于返回什么：如果找到了符合要求的值，此时left == right；但要退出循环还要再运行一次，所以会造成left+1偏移
    #因此最后right指向的是正确的结果
    #左闭右开区间也同样分析

N, K = map(int, input().split())
array = list(map(int, input().split()))
res = binary_search(array, K)
print(res)
