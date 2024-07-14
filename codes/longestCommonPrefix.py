class Solution: #prefix
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        prefix=''
        a1=strs[0]
        an=strs[-1]
        for i in range(len(a1)):
            if a1[i]!=an[i]:
                return prefix
            else:
                prefix+=a1[i]
        return prefix

if __name__=="__main__":
    pass
