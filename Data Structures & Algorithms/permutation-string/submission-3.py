class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        lens = len(s1)
        r = lens
        check1 = {}
        
        for i in range(len(s1)):
            check1[s1[i]] = 1 + check1.get(s1[i] , 0)
        for r in range(lens-1, len(s2)):
            check2 = {}
            for j in range(l,r+1):
                check2[s2[j]] = 1 + check2.get(s2[j] , 0)
            if check1 == check2:
                return True
            l += 1
        return False