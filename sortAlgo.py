# 排序类算法

# 快排模板
# leetcode: 215题, 480题
def quik_sort(nums, left, right):
    if left >= right:
        return
    mid_value = nums[left]
    start = left
    end = right
    while left < right:
        # print(left, right)
        while left < right and nums[right] >= mid_value:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= mid_value:
            left += 1
        nums[right] = nums[left]
    # 跳出循环时left = right
    nums[left] = mid_value
    quik_sort(nums, start, left - 1)
    quik_sort(nums, left + 1, end)

# 二分查找, nums为递增数组
# leetcode: 34题, 480题
def binarySearch(nums, left, right, n):
    if left > right: return -1

    mid_pos = (left + right)//2
    # print(mid_pos)
    mid_value = nums[mid_pos]
    if mid_value == n:
        return mid_pos
    elif mid_value > n:
        return binarySearch(nums, left, mid_pos - 1, n)
    else:
        return binarySearch(nums, mid_pos+1, right, n)


if __name__ == "__main__":
    nums = [3, 7, 6, 3]
    quik_sort(nums, 0, 3)
    print(nums)
    print(binarySearch(nums, 0, 3, 3))