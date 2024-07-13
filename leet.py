import os
from  statistics import median
os.system('cls')
class Solution1: #roman
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

class Solution: #MedianSortedArrays
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3)%2!=0:
            return (nums3[(len(nums3)//2)])
        else:
            return ((nums3[(len(nums3)//2)]+nums3[(len(nums3)//2)-1])/2)
        
class Solution: #longestPalindrome
    def longestPalindrome(self, s: str) -> str:
        def geser(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        result=""
        for i in range (len(s)):
            sub1=geser(i,i)
            if len(sub1) > len(result):
                result=sub1
            sub2=geser(i,i+1)
            if len(sub2) > len(result):
                result=sub2
        return result

class Solution: #zigzag string
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or numRows >len(s):
            return (s)
        data=[[] for i in range(numRows)]
        index=0
        step=1
        for char in s:
            data[index].append(char)
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step

        for i in range(numRows):
            data[i]="".join(data[i])
        return "".join(data)

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

class Solution: #atoi function
    def myAtoi(self,s:str)->int:
        s=s.lstrip() #remove leading, default (" ")
      
        if not s: #kalo kosong
            return 0

        a=""
        operator=["-","+"]
        i=0

        if s[i] in operator: #determine postive or negative number
            a+=s[i]
            i+=1
        
        while i < len(s) and s[i].isdigit():
            a+=s[i]
            i+=1

        # Check if a is empty or just a sign
        if len(a) == 0 or a == "-" or a == "+":
            return 0
        a=int(a)    

        if a <-2**31:
            a=-2**31
        elif a >2**31-1:
            a=2**31-1
        
        return a

class Solution: #max area
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        baskom=0
    
        while l<r:
            baskom_temp=min(height[l],height[r])*(r-l)
            baskom=max(baskom,baskom_temp)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return baskom

class Solution: #int-->roman
    def intToRoman(self, num: int) -> str:
        res=""
        romans = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]

        for i,j in reversed(romans):
            while num>=j:
                res+=i
                num-=j
        return res

 
# input
if __name__=="__main__":
    num=3749
    sol=Solution()
    print(sol.intToRoman(num))
    input()


