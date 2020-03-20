from typing import List
import collections

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





if __name__ == "__main__":
    matrix = [["0","1"]]
    example = Solution()
    a = example.maximalSquare(matrix)
