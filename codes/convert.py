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