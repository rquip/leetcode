# SOLUTION TWO
# Trying to go from O(n**2) to O(n)
# Using one pass hash
class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            nums_hash = {}
            new_indice = 0
            for elements_of_nums in nums:
                other_value = target - elements_of_nums
                try:
                    nums_hash[elements_of_nums]
                    if 2*elements_of_nums == target:
                        return([nums_hash[elements_of_nums], new_indice])
                    else:
                    	new_indice = new_indice + 1
                except KeyError:
                    nums_hash[elements_of_nums] = new_indice
                    new_indice = new_indice + 1
                    if len(nums_hash) > 1 and other_value != elements_of_nums:
                    	try: 
                        	nums_hash[other_value]
                        	return([nums_hash[other_value], nums_hash[elements_of_nums]])
                    	except KeyError:
                        	continue
