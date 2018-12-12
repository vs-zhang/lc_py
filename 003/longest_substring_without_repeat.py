class Solution(object):
    def longest_substring_without_repeat(self, str):
        d = {}
        start = 0
        ans = 0
        for i, c in enumerate(str):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)
        return ans


s = Solution()
ans = s.longest_substring_without_repeat('pwwkew')
ans2 = s.longest_substring_without_repeat('abcabcbb')
ans3 = s.longest_substring_without_repeat('bbbbb')
print(ans)
print(ans2)
print(ans3)