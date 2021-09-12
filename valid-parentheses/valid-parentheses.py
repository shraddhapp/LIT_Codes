class Solution:
    def isValid(self, s: str) -> bool:
        out_dict = { '(':')', '[':']', '{':'}' }
        stack = []


        for char in s:
            if char in out_dict:
                stack.append(char)
            else:
                if stack:
                    c = stack.pop()
                    if(char != out_dict[c]):
                        return False
                else:
                    return False
                
        if not stack:
            return True
        else:
            return False