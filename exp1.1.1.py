def bruteforce(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


def hashmap(nums, k):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True
        seen[nums[i]] = i
    return False


def slidingwindow(nums, k):
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i - k])
    return False


nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
r1 = bruteforce(nums, k)
print("Brute Force:", r1)
r2 = hashmap(nums, k)
print("Hash Map:", r2)
r3 = slidingwindow(nums, k)
print("Sliding Window:", r3)
