class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i= 0
        j= len(nums)-1
        mid=(j+i)//2
        while j>=i:
            if target == nums[mid]:
                return mid
            if target>nums[mid]:
                i= mid+1
            else:
                j= mid-1
            mid= (j+i)//2
        return -1
