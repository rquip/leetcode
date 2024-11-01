# Problems: Can't do any string with digits, space or symbols

import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set up alphabet comparison dictionary
        alphabet_dict = {y:x for x,y in enumerate(string.ascii_lowercase)}

        # main algorithm
        sequence_total = 1
        largest_sum = 1
        comparer = None
        for letter_index in range(len(s)):
            if letter_index == len(s)-1:
                if largest_sum < sequence_total:
                    largest_sum = sequence_total
                    sequence_total = 1
                    break
                else:
                    break
            elif sequence_total == 1:
                a = alphabet_dict[s[letter_index]]
                b = alphabet_dict[s[letter_index+1]]
                if a > b:
                    comparer = "greater"
                    sequence_total = sequence_total + 1
                elif a < b:
                    comparer = "less"
                    sequence_total = sequence_total + 1
            else:
                a = alphabet_dict[s[letter_index]]
                b = alphabet_dict[s[letter_index+1]]
                if comparer == "less":
                    if a < b:
                        sequence_total = sequence_total + 1
                    else:
                        comparer = None
                        if largest_sum < sequence_total:
                            largest_sum = sequence_total
                            sequence_total = 1
                        else:
                            sequence_total = 1
                elif comparer == "greater":
                    if a > b:
                        sequence_total = sequence_total + 1
                    else:
                        comparer = None
                        if largest_sum < sequence_total:
                            largest_sum = sequence_total
                            sequence_total = 1
                        sequence_total = 1

        return(largest_sum)                    
                    

