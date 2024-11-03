import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temporary_string = ""
        largest_sum = 1
        iterative_value = 0
        while True:
            if len(s) == 0:
                return(0)
            elif iterative_value == len(s):
                return(largest_sum)
            else:
                for x in range(iterative_value, len(s)):
                    if s[x] in temporary_string:
                        if len(temporary_string) > largest_sum:
                            largest_sum = len(temporary_string)
                            iterative_value = iterative_value + 1
                            temporary_string = ""
                            break
                        else:
                            iterative_value = iterative_value + 1
                            temporary_string = ""
                            break
                    else:
                        temporary_string = temporary_string + s[x]
