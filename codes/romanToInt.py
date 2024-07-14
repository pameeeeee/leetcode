class Solution: #roman
    def romanToInt(self, s: str) -> int:
        kamus={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        total = 0
        for i in range(len(s)-1):
            if kamus[s[i]]<kamus[s[i+1]]:
                total -= kamus[s[i]]
            else:
                total+=kamus[s[i]]
        return total + kamus[s[i+1]]

if __name__=="__main__":
    pass
