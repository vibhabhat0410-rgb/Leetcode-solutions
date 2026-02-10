# Problem: Two Sum
# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in seen:
            return [seen[rem], i]
        seen[num] = i
