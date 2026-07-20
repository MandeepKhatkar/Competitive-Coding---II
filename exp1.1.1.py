def containsNearbyDuplicate_bruteforce(nums, k):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True

    return False


def containsNearbyDuplicate_hashmap(nums, k):
    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True

        seen[nums[i]] = i

    return False


def containsNearbyDuplicate_slidingwindow(nums, k):
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

print("\nResults")
print("----------------------------------------")

result1 = containsNearbyDuplicate_bruteforce(nums, k)
print("Approach 1 (Brute Force)        :", result1)

result2 = containsNearbyDuplicate_hashmap(nums, k)
print("Approach 2 (Hash Map)           :", result2)

result3 = containsNearbyDuplicate_slidingwindow(nums, k)
print("Approach 3 (Sliding Window)     :", result3)

print("----------------------------------------")