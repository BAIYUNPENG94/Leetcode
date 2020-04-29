from typing import List
import collections

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.lead, self.times, counts = [], times, {}
        leadperson = -1
        for candidate, time in zip(persons, times):
            counts[candidate] = counts.get(candidate, 0) + 1 
            if counts.get(leadperson, 0) <= counts[candidate]:
                leadperson = candidate
            self.lead.append(leadperson)
    def q(self, t: int) -> int:
        leftindex, rightindex = 0, len(self.times) - 1
        while leftindex <= rightindex:
            midindex = (leftindex + rightindex) // 2
            if self.times[midindex] == t:
                return self.lead[midindex]
            elif midindex > t:
                rightindex -= 1
            else:
                leftindex += 1
            return self.lead[leftindex-1]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Node:
    def __init__(self, val: int = 0, left: 'Node'= None, right: 'Node' = None, next: 'Node' = None):
        self.val = val 
        self.left = left 
        self.right = right 
        self.next = next 

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        poslistA = []
        poslistB = []
        lendic = collections.defaultdict(int)
        for i in range(n * n):
            if A[int(i/n)][i%n] == 1: 
                poslistA.append((int(i/n))*100+(i%n))
            if B[int(i/n)][i%n] == 1:
                poslistB.append((int(i/n))*100+(i%n)) 
        if not poslistA or not poslistB:
            return 0
        for nodeA in poslistA:
            for nodeB in poslistB:
                lendic[nodeB - nodeA] += 1
        return max(lendic.values())

    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = 0
        rightmax = 0
        result = 0
        leftmhight = [0 for i in range(n)]
        for i in range(n):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmhight[i] = leftmax
        for i in reversed(range(n)):
            if height[i] > rightmax:
                rightmax = height[i]
            if height[i] < min(rightmax, leftmhight[i]):
                result += min(rightmax, leftmhight[i]) - height[i]
        return result

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        size = [[0 for i in range(m)] for j in range(n)] 
        ans = 0
        for i in range(n):
            for j in range(m):
                size[i][j] = int(matrix[i][j])
                if size[i][j] == 0:
                    continue
                elif i == 0 or j == 0:
                    size[i][j] = 1
                else:
                    size[i][j] += min(size[i-1][j],
                    size[i][j-1], size[i-1][j-1])
                ans = max(ans, size[i][j]*size[i][j])
        return ans

    def merge(self, num1: List[int], n: int, num2: List[int], m: int) -> None:
        while n > 0 and m > 0:
            if num1[n-1] <= num2[m-1]:
                num1[m+n-1] = num2[m-1]
                m -= 1
            else:
                num1[m+n-1] = num1[n-1]
                n -= 1
        num1[:m] = num2[:m]

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        ans = []
        def countnums(gridline:List[str]):
            if gridline == []:
                return 0
            if gridline.count('W') != 0:
                index = gridline.index('W')
                return gridline[:index].count('E')
            else:
                return gridline.count('E')
        n, m = len(grid), len(grid[0])
        for x in range(n):
            for y in range(m):
                nums = 0
                if grid[x][y] == 'E' or grid[x][y] == 'W':
                    continue
                else:
                    if y != m-1:
                        nums += countnums(grid[x][y+1:])
                    if y != 0:
                        a = grid[x][:y]
                        a = a[::-1]
                        nums += countnums(a)
                        #print(nums)
                    if x != n-1:
                        nums += countnums([a[y] for a in grid[x+1:]])
                    if x != 0:
                        a = [a[y] for a in grid[:x]]
                        a = a[::-1]
                        nums += countnums(a)
                    ans.append(nums)
        if ans == []:
            return 0
        return max(ans)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Sdict = collections.defaultdict(int)
        Tdict = collections.defaultdict(int)
        for i in range(len(s)):
            Sdict[s[i]] += 1
            Tdict[t[i]] += 1
        if Sdict == Tdict:
            return True
        else:
            return False
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def countans(root):
            if root == None:
                return 0
            ans = max(countans(root.left), countans(root.right))
            if root.left == None:
                root.leftmax = 0
            else:
                root.leftmax = max(root.left.leftmax, root.left.rightmax) + 1
            if root.right == None:
                root.rightmax = 0
            else:
                root.rightmax = max(root.right.leftmax, root.right.rightmax) + 1
            if root.rightmax + root.leftmax > ans:
                ans = root.rightmax + root.leftmax
            return ans
        result = countans(root)
        return result

    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root == None:
                return None
            temp = invert(root.left)
            root.left = invert(root.right)
            root.right = temp
            return root
        root = invert(root)
        return root
    
    def fizzBuzz(self, n: int) -> List[str]:
        result = ["" for i in range(n)]
        for i in range(n):
            if (i+1) % 15 == 0:
                result[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                result[i] = "Fizz"
            elif (i+1) % 5 == 0:
                result[i] = "Buzz"
            else:
                result[i] = str(i+1)
        return result

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True 
        if not s or not t:
            return False 
        return self.isSametree(s, t) or self.isSametree(s.left, t) or self.isSametree(s.right, t)
        

    def isSametree(self, s: TreeNode, t: TreeNode):
        if not s and not t:
            return True
        if not s or not t:
            return False 
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
    
    def reverselist(self, Dummy, start, end):
        while start != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = start
            Dummy.next = tmp

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        Answer, Dummy = ListNode(0), ListNode(0)
        Dummy.next = head
        start, end = head, head
        count = 1
        while(1):
            if count % k == 0:
                reverselist(Dummy, start, end)
                if count / k == 1:
                    Answer = Dummy 
                Dummy = end
                end = end.next
            else:
                count += 1
                start = start.next
            if start == None or start.next == None:
                break
        return Answer.next

    def twoSum(self, nums:List[int], target: int) -> List[int]:
        MatchSet = {}
        for index in range(len(nums)):
            if nums[index] in MatchSet:
                answer = [MatchSet[nums[index]], index]
            else:
                MatchSet[target-nums[index]] = index
        return answer

    #def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        







if __name__ == "__main__":
    a = 15.24 * 50000
    print(a/4)
