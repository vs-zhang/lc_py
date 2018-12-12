class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        sign = 1
        ans = 0
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        for c in s:
            if c.isdigit():
                ans = ans * 10 + int(c)
            else:
                break
        ans = sign*ans
        return ans


s = Solution()
ans = s.myAtoi('-1234')
print(ans)