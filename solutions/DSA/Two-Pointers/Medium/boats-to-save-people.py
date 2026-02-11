# LeetCode #881 - Boats to Save People
# Pattern: Two Pointers (Greedy)
# Difficulty: Medium
# Date Solved: Feb 2, 2026

# Approach:
# - Sort the array
# - Use two pointers (lightest + heaviest)
# - If they fit together, pair them; otherwise heavy person rides alone
# - Time: O(n log n) | Space: O(1)

def numRescue(nums, limit):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left <= right:
        if nums[left] + nums[right] <= limit:
            left += 1
            right -= 1
            count += 1
        else:
            right -= 1
            count += 1

    return count

# Test
print(numRescue([3, 2, 2, 1], 3))  # Output: 3
