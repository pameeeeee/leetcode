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