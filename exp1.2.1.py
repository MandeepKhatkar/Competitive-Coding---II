def search_linear(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def search_binary(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


nums = [1,2,3,4,5,6,7,8,9]
target = 2
lr = search_linear(nums, target)
br = search_binary(nums, target)
print("Linear Search:", lr)
print("Binary Search:", br)