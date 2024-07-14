class Solution: #bukatutup bracket
    def parentheses(self, s: str) -> bool:
        char={'(':')',
        '{':'}',
        '[':']'
        }
        stack=[]
        for i in s:
            if i in char:
                stack.append(i)
            elif len(stack)==0 or i != char[stack.pop()]:
                return False
        return len(stack) ==0

if __name__=="__main__":
    pass
