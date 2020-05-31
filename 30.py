from typing import List

class Solution:
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

    def isHappy(self, n: int) -> bool:
        def makesum(x: int) -> int:
            Sum = 0
            cha = str(x)
            for i in cha:
                Sum += int(i) * int(i)
            return Sum
        x = n
        dock = []
        while(x not in dock[:-1]):
            x = makesum(x)
            print(x)
            dock.append(x)
            print(dock)
            if x == 1:
                return True
        return False

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        Sum = nums[0]
        for index in range(1, len(nums)):
            Sum = max(nums[index], Sum+nums[index])
            if Sum > ans:
                ans = Sum
        return ans

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastzero = 0
        for index in range(1, len(nums)):
            if nums[index] != 0:
                nums[lastzero], nums[index] = nums[index], nums[lastzero]
                lastzero += 1

    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 0
        for index in range(len(prices)-1):
            if prices[index+1] < prices[index]:
                sell = index
                profit += prices[sell] - prices[buy]
                buy = index + 1
            elif index+1 == len(prices)-1:
                sell = index + 1
                profit += prices[sell] - prices[buy]
        return profit

    def groupAnagrams(self, strs: List[str]):
        result = [[]]
        data = {}
        index = 0
        for substr in strs:
            vari = sorted(substr)
            gg = ''.join(vari)
            if gg in data:
                result[data[gg]].append(substr)
            else:
                data[gg] = index
                if index == 0:
                    result[data[gg]].append(substr)
                else:
                    result.append([])
                    result[data[gg]].append(substr)
                index += 1
        return result

    def countElements(self, arr: List[int]) -> int:
        data = {}
        count = 0
        arr = sorted(arr, reverse=True)
        for num in arr:
            if num+1 in data:
                count += 1
                data[num] = 1
            else:
                data[num] = 1
        return count

    def backspaceCompare(self, S: str, T: str) -> bool:
        def dotheinput(S: str):
            temp = ''
            for cha in S:
                if cha == '#':
                    if len(temp) != 0:
                        temp = temp[:-1]
                else:
            return temp
        return dotheinput(S) == dotheinput(T)

    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        maxdep = 0

        def getdown(root, maxdep):
            if root == None:
                return maxdep
            else:
                maxdep += 1
                return max(getdown(root.left, maxdep), getdown(root.right, maxdep))
        return getdown(root, maxdep)

    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        stack = []
        pairing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for cha in s:
            if cha in pairing:
                if stack == []:
                    return False
                chapair = stack.pop()
                if pairing[cha] != chapair:
                    return False
            else:
                stack.append(cha)
        return not stack
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>= 2:
            Max01 = max(stones)
            stones.remove(Max01)
            Max02 = max(stones)
            stones.remove(Max02)
            remain = abs(Max02-Max01)
            if remain == 0:
                continue
            else:
                stones.append(remain)
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0] 
    
    def findMaxLength(self, nums: List[int]) -> int:
        Sum, Answer = 0, 0
        Step = {0: -1}
        for index in range(len(nums)):
            if nums[index] == 1:
                Sum += 1
            else: Sum -= 1
            if Sum in Step:
                Answer = max(Answer, index - Step[Sum])
            else: Step[Sum] = index
        return Answer

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        movemove = 0
        for shit in shift:
            if shit[0] == 0:
                movemove -= shit[1]
            else: movemove += shit[1]
        if movemove < 0:
            movemove = abs(movemove) % len(s)
            s = s[movemove:] + s[:movemove]
        elif movemove > 0:
            movemove = abs(movemove) % len(s)
            s = s[-movemove:] + s[:-movemove]
        return s

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for i in range(len(nums))]
        tmp = 1
        for index in range(len(nums)):
            answer[index] *= tmp
            tmp *= answer[index]
        tmp = 1
        for index in range(len(nums)-1, -1, -1):
            answer[index] *= tmp
            tmp *= answer[index]
        return answer

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:




if __name__ == "__main__":
    project = Solution()
    a = project.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(a)
