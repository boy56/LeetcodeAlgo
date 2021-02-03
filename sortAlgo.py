# 排序类算法

# 快排模板
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



if __name__ == "__main__":
    nums = [3, 7, 6, 3]
    quik_sort(nums, 0, 3)
    print(nums)