class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

a = Solution()
print(a.getConcatenation(nums = [1,2,1]))
# Output: [1,2,1,1,2,1]
print(a.getConcatenation(nums = [1,3,2,1]))
# Output: [1,3,2,1,1,3,2,1]
