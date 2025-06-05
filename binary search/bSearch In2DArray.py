class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot= 0, len(matrix)-1
        while bot>=top:
            mid= (top+bot)//2
            if matrix[mid][-1]<target:
                top= mid+1
            elif matrix[mid][0]>target:
                bot= mid-1
            else:
                if not bot>=top:
                    return False
                l=0
                r=len(matrix[mid])-1
                while(r>=l):
                    m= (l+r)//2
                    if target>matrix[mid][m]:
                        l=m+1
                    elif target<matrix[mid][m]:
                        r=m-1
                    elif target == matrix[mid][m]:
                        return True
                return False
        return False 