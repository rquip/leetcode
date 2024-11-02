# New problem with code: I had assumed the problem is a value-sequential problem. It actually is once a symbol is repeated, the length is done -- I'm going to redo it. This solution does work given the assumptions I have.

import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set up alphabet/number/symbol comparison dictionary
        if len(s) == 0: return(0)
        alphabet_dict = {y:x+1 for x,y in enumerate(string.ascii_lowercase)}
        misc_list = [x for x in string.punctuation]
        misc_list.append(" ")
        alphabet_dict.update({c:0 for c in misc_list})
        alphabet_dict.update({str(d):0 for d in range(0,10)})
        symbol_and_number = {e:0 for e in misc_list}
        symbol_and_number.update({str(d):0 for d in range(0,10)})
        
        # main algorithm
        sequence_total = 1
        largest_sum = 1
        comparer = None
        for letter_index in range(len(s)):
            # print("character = " + s[letter_index])
            # print("sequence_total = " + str(sequence_total))
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
                if (s[letter_index] in symbol_and_number) and (s[letter_index + 1] in symbol_and_number) and s[letter_index] == s[letter_index + 1]:
                    if largest_sum < sequence_total:
                        largest_sum = sequence_total
                        sequence_total = 1
                    else:
                        sequence_total = 1
                elif ((s[letter_index] in symbol_and_number) or (s[letter_index + 1] in symbol_and_number)) and s[letter_index] != s[letter_index + 1]:
                    sequence_total = sequence_total + 1
                elif comparer == "less":
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
                    

