class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [(p,s) for p,s in zip(position, speed)]
        posSpeed.sort(reverse=True)
        stack=[]
        print(posSpeed)
        for ele in posSpeed:
            print(ele[0],ele[1])
            currTime= (target-ele[0])/ele[1]
            print(currTime, stack[-1] if stack else "")
            
            if stack and currTime <= stack[-1]:
                print("in the if condition", stack[-1])
                continue
            stack.append(currTime)
        return len(stack)
        