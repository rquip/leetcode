# SOLUTION ONE
# Complexity: O(n**2)
# Class of solution: Brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return([x, y])  # Return the indices if a match is found
        # if no two elements sum up to target
        print("No elements of nums add up to target")
        return(None)  # Return None if no solution is found
