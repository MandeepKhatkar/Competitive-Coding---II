def bruteforce(nums):
    n = len(nums)
    answer = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        answer.append(product)
    return answer


def prefix_suffix(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]
    return answer


def optimized(nums):
    n = len(nums)
    answer = [1] * n    
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]  
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    return answer


nums = list(map(int, input("Enter array elements separated by spaces: ").split()))
r1 = bruteforce(nums)
print("Brute Force:", r1)
r2 = prefix_suffix(nums)
print("Prefix-Suffix Arrays:", r2)
r3 = optimized(nums)
print("Optimized:", r3)
