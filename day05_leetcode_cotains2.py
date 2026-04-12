class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = set(nums)
        return True if len(nums) > len(set(nums)) else False
    


s = Solution()
print(s.containsDuplicate([1,5,6,8])) 
print(s.containsDuplicate([1,5,1,8])) 
