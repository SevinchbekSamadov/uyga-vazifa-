class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            s = 0
            for i in range(len(str(n))):
                s += int(str(n)[i]) ** 2
            n = s
        if n == 1 or n == 7:
            return True
        else:
            return False


test1 = Solution()
print(test1.isHappy(19))
#True
print(test1.isHappy(2)) 
#False