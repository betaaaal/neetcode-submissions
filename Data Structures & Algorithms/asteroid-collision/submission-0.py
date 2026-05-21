class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l=[]
        for a in asteroids:
            if a>0:
                l.append(a)
            else:
                while l and l[-1]>0 and abs(l[-1])<abs(a):
                    l.pop()
                if l and l[-1]>0 and abs(l[-1])==abs(a):
                    l.pop()
                elif not l or l[-1]<0:
                    l.append(a)
        return l
