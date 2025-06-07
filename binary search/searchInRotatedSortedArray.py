class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        m=(l+r)//2
        while(l<=r):
            m=(l+r)//2
            if nums[m] == target:
                return m
            if nums[l]<=nums[m]:
                if target>=nums[l] and target<=nums[m]:
                    if target == nums[m]:
                        return m
                    r=m-1
                else:
                    l=m+1
                    continue
            if nums[m]<=nums[r]:
                    if target>=nums[m] and target<=nums[r]:
                        if target == nums[m]:
                            return m
                        l=m+1
                    else:
                        r=m-1
              
        return -1

