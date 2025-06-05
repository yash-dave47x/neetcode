class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper=max(piles)
        l,r= 1,upper
        m=-1
        ans=-1
        while(l<=r):
            m= (l+r)//2
            time=0
            for num in piles:
                time+=math.ceil(num/m)
            if time>h:
                l=m+1
            elif time<=h:
                r=m-1
                ans=m
        return ans
            