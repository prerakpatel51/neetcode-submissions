class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their opening pairs
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop from stack if not empty, else use dummy character
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing one
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)

        # Valid only if no opening brackets remain
        return not stack
