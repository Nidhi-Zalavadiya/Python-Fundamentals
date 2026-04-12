
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    def twoSumSmart(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need],i]
            seen[nums[i]] = i


s1 = Solution()
print(s1.twoSum([2,7,11,15],10))
