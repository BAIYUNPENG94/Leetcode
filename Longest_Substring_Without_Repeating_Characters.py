class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        stock = set()
        length = 0
        while start < len(s) and end < len(s):
            if s[end] in stock:
                length = max(length, (end - start))
                stock.remove(s[start])
                start += 1
            else:
                stock.add(s[end])
                end += 1
        return max(length, (end - start))
