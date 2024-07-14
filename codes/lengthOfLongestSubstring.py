class Solution: #panjangsubstring
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        l=0
        panjang=0
        for r in range (len(s)):
            char=s[r]
            if char in seen and seen[char] >=l:
                l = seen[char]+1
            else:
                panjang= max(panjang, r-l+1)
            seen[char]=r
        return panjang

if __name__=="__main__":
    pass
