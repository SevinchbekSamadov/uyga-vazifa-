class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a = [i for i in range(len(nums) + 1)]
        for j in range(len(nums)):
            a.remove(nums[j])
        return a[0] 

a = Solution()
print(a.missingNumber(nums = [3,0,1]))
#2
print(a.missingNumber(nums = [0,1]))
#2
