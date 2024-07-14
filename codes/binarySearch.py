class Solution: #binarysearch
    def binarySearch (self,s:list, target:int):
        return self.searching(s,0,len(s)-1,target)

    def searching(self,s,l,r,target): #l pointer kiri r pointer kanan
        while l <=r:
            a=(l+r)//2
            if s[a]==target:
                return "Target Ditemukan:",s[a]
            elif s[a] > target:
                r=a-1
            else:
                l=a+1
            print(s[a],s[l:r+1])
        return "Target Tidak Ditemukan"
