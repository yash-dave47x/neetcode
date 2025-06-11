class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        max_length=0
        hasSeen={}
        
        for ind,val in enumerate(s):
            r=ind
            if val in hasSeen and l<=hasSeen[val]:
                oldPos=hasSeen[val]
                print("seen value", val, oldPos)
                l=oldPos+1
                hasSeen[val]= ind
                print("current ind", val, ind)
            else:
                hasSeen[val]= ind
            length= r-l+1
            if max_length<length:
                max_length = length
                print("r",r,"l",l, "len", max_length)


        return max_length                