# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Take l1 and go through it and save it as a number

        first_number = []
        second_number = []
        while True:
            first_number.append(l1.val)
            if l1.next == None:
                break
            else:
                l1 = l1.next
        first_number.reverse()
        while True:
            second_number.append(l2.val)
            if l2.next == None:
                break
            else:
                l2 = l2.next
        second_number.reverse()
        second_number_string = ''
        for x in second_number:
            second_number_string = second_number_string + str(x)
        first_number_string = ''
        for y in first_number:
            first_number_string = first_number_string + str(y)
        summation = int(first_number_string) + int(second_number_string)

        # Now need to make a linked list from summation

        summation_as_list = list(str(summation))
        summation_as_list.reverse()
        origin = ListNode()
        temp = origin
        for w in range(len(summation_as_list)):
            if w != len(summation_as_list)-1:
                temp.val = int(summation_as_list[w])
                temp.next = ListNode()
                temp = temp.next
            elif w == len(summation_as_list)-1:
                temp.val = int(summation_as_list[w])
                temp.next = None
        
        return(origin)
        
