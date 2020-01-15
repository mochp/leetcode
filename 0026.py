class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length==0:
            return 0
        i = 0
        for j in range(length):
            if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1