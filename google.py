from typing import List
import itertools


class StringIterator:

    def __init__(self, compressedString: str):

    def next(self) -> str:

    def hasNext(self) -> bool:


class NumArray:
    val = []

    def __init__(self, nums: List[int]):
        self.val = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.val[i:j+1])


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        s = set(nums1)
        for n in nums2:
            if n in s:
                result.append(n)
                s.discard(n)
        return result

    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        result = []
        for n in digits:
            s += str(n)
        s = str(int(s) + 1)
        for x in s:
            result.append(int(x))
        return result

    def isIsomorphic(self, s: str, t: str) -> bool:
        dd = dict()
        for i in range(len(s)):
            if s[i] in dd:
                if t[i] == dd[s[i]]:
                    continue
                else:
                    return False
            else:
                if t[i] in dd.values():
                    return False
                else:
                    dd[s[i]] = t[i]
        return True

    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            res = "".join((str(len(list(group)))+str(digit) for
                           digit, group in itertools.groupby(res)))
        return res
