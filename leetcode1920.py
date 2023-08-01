class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        a = []
        for i in range(len(nums)):
            a.append(nums[nums[i]])
        return a
        

a = Solution()
print(a.buildArray(nums = [0,2,1,5,3,4]))
# Output: [0,1,2,4,5,3]
print(a.buildArray(nums = [5,0,1,2,3,4]))
# Output: [4,5,0,1,2,3]