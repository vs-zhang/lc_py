class Solution(object):
    def reverse_number(self, num):
        sign = -1 if num < 0 else 1
        ans = 0
        num = abs(num)
        while num:
            ans = ans*10 + num % 10
            num = num // 10
        return sign * ans


s = Solution()
n = s.reverse_number(123)
print(n)