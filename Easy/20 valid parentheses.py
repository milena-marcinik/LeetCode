"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_parenthesis = ["(", "[", "{"]
        right_parenthesis = [")", "]", "}"]

        for char in s:
            if char in left_parenthesis:
                stack.append(char)
            elif char in right_parenthesis:
                position = right_parenthesis.index(char)
                if len(stack) > 0 and left_parenthesis[position] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
