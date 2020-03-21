from typing import List
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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






if __name__ == "__main__":
    grid = [["W","E","E","E","E","0","E","E","E","E","E","W"]] 
    example = Solution()
    a = example.maxKilledEnemies(grid)
    print(a)
