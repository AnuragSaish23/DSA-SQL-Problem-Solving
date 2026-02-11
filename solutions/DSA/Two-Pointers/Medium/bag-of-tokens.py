# LeetCode #948 - Bag of Tokens
# Pattern: Two Pointers (Greedy)
# Difficulty: Medium
# Date Solved: Feb 2, 2026

# Approach:
# - Sort tokens
# - Left pointer: play face-up (spend power, gain score) — use cheap tokens
# - Right pointer: play face-down (spend score, gain power) — sell expensive tokens
# - Track maxScore since score fluctuates
# - Time: O(n log n) | Space: O(1)

def bagoftokens(tokens, power):
    tokens.sort()
    left, right = 0, len(tokens) - 1
    score = maxScore = 0

    while left <= right:
        if power >= tokens[left]:
            score += 1
            power -= tokens[left]
            maxScore = max(score, maxScore)
            left += 1
        elif score >= 1 and left < right:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return maxScore

# Test
print(bagoftokens([100, 200, 300, 400], 200))  # Output: 2
