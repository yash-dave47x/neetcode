class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r= 0, len(nums)-1
        res=nums[(l+r)//2]
        while(r>=l):
            m=(l+r)//2
            if nums[m]>=nums[l]:
                if res>nums[l]:
                    res= nums[l]
                l=m+1
            else:
                if res>=nums[m]:
                    res=nums[m]
                r=m-1
        return res
