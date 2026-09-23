class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                if a>0:
                    stack.append(a)
                else:
                    if 0>stack[-1]:
                        stack.append(a)
                    else:
                        while stack and stack[-1] > 0 and (a+stack[-1] <0):
                            stack.pop()
                        if stack and a+stack[-1]>0:
                            continue
                        elif stack and a+stack[-1]==0:
                            stack.pop()
                        else:
                            stack.append(a)
                        
        return stack