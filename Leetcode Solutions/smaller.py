class Solution:
    def smallerNumbersThanCurrent(self, n: List[int]) -> List[int]:
        lst=[0]*len(n)
        k=0
        for i in n:
            k=k+1
            for j in n: 
                if i>j:
                    lst[k-1]=lst[k-1]+1
        return(lst)
#n=list(map(int,input('nums = ').strip().split()))
