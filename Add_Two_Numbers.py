# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        Sum = l1.val
        Sum += l2.val
        ans.val = Sum % 10
        tmp = Sum // 10
        l1 = l1.next
        l2 = l2.next
        if l1 == None and l2 == None:
            if tmp == 0:
                return ans
            else:
                ans.next = ListNode(tmp)
                return ans
        ans.next = ListNode(0)
        lin = ans.next
        Sum = 0
        while True:
            if l1 != None:
                Sum += l1.val
                l1 = l1.next
            if l2 != None:
                Sum += l2.val
                l2 = l2.next
            Sum += tmp
            lin.val = Sum % 10
            tmp = Sum // 10
            if l1 == None and l2 == None:
                if tmp == 0:
                    return ans
                else:   
                    lin.next = ListNode(tmp)
                    return ans
            lin.next = ListNode(0)
            lin = lin.next
            Sum = 0
