def searchBinary(nums,target):
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
    return -1


def searchBruteForce(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [1,2,3,4,0,1,2,3,4,5]
target = 2
print("Binary Result:",searchBinary(nums, target))
print("Brute Result:",searchBruteForce(nums, target))