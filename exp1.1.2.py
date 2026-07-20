def productExceptSelf_bruteforce(nums):

    n = len(nums)
    answer = []

    for i in range(n):

        product = 1

        for j in range(n):

            if i != j:
                product *= nums[j]

        answer.append(product)

    return answer


def productExceptSelf_prefix_suffix(nums):

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


def productExceptSelf_optimized(nums):

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

print("\nResults")
print("-----------------------------------------------")

result1 = productExceptSelf_bruteforce(nums)
print("Approach 1 (Brute Force)           :", result1)

result2 = productExceptSelf_prefix_suffix(nums)
print("Approach 2 (Prefix-Suffix Arrays)  :", result2)

result3 = productExceptSelf_optimized(nums)
print("Approach 3 (Optimized)             :", result3)

print("-----------------------------------------------")