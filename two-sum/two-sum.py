'''
# SOLUTION ONE
# Complexity: O(n**2)
# Class of solution: Brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # error checking
        if len(nums) < 2:
            print("nums needs to be at least 2 elements")
            exit()  # Exit if nums has fewer than 2 elements
        
        # the two sum
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return([x, y])  # Return the indices if a match is found
        
        # if no two elements sum up to target
        print("No elements of nums add up to target")
        return(None)  # Return None if no solution is found
'''

# SOLUTION TWO
# Doesn't seem to work for negative numbers. I didn't realize I need to use negative integers.
# Complexity: Likely worse. O(T*n)
# Class of solution: Attempted to shorten brute force to linear time and failed
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(target//2 + 1):
            if target%2 == 0 and x == target//2 and nums.count(x) == 2:
                try:
                    first_index = nums.index(x)
                    return([first_index, nums[first_index+1:].index(x)+first_index+1])
                except ValueError:
                    print("No solution")
            else:
                try:
                    first = nums.index(x)
                    second = nums.index(target-x)
                    return([nums.index(x), nums.index(target-x)])
                    break
                except ValueError:
                    continue


'''
# NOTES
[X] Need to figure out how the class definition above works
[X] Need to figure out how to calculate complexity
[/] See if you can speed up code
- Learn again how to submit this to github
- Look up hash maps
- Look up optimizing searches
- 
'''
