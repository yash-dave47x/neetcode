class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack=[]
        sol=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if not tempStack:
                tempStack.append(i)
                continue
            while tempStack and temperatures[i]> temperatures[tempStack[-1]]:
                sol[tempStack[-1]]= i-tempStack[-1]
                tempStack.pop()
            tempStack.append(i)

        return sol
