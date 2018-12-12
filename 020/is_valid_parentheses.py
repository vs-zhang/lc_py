class Solution(object):
    def is_valid_parentheses(self, s):
        stack = []
        pair = ['()', '[]', '{}']
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in pair:
                stack.pop()
                stack.pop()
        return len(stack) == 0


s = Solution()
print(s.is_valid_parentheses('()'))
print(s.is_valid_parentheses('([])'))
print(s.is_valid_parentheses('([)'))
