class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []

        if len(s) < 2: 
            return False

        for _s in s:
            try:
                if _s != ")" and _s != "}" and _s != "]":
                    stack.append(_s)
                else:
                    if _s == ")" and stack[-1] != "(": return False
                    elif _s == "}" and stack[-1] != "{": return False
                    elif _s == "]" and stack[-1] != "[": return False
                    else: stack.pop(-1)
            except: return False

        if len(stack) > 0: return False
        return True
        
