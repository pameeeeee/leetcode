class Solution: #reverse int
    def reverse(self, x: int) -> int:
        if x < 0:
            x=int(str(x)[:0:-1]) * -1
        else:
            x=int(str(x)[::-1])
            
        if x <=2**31 and x >=-2**31-1:
            return x
        else:
            return 0