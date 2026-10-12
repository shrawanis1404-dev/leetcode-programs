
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0


# VS Code testing
obj = Solution()
print(obj.isValid("()"))
print(obj.isValid("()[]{}"))
print(obj.isValid("(]"))
print(obj.isValid("({[]})"))
