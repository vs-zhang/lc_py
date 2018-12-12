class Solution(object):
    def is_palindrome_number(self, num):
        half = 0
        while num > half:
            half = half * 10 + num % 10
            num = num // 10
        return num == half or half // 10 == num


s = Solution()
print(s.is_palindrome_number(1234321))
print(s.is_palindrome_number(123321))
print(s.is_palindrome_number(123921))
