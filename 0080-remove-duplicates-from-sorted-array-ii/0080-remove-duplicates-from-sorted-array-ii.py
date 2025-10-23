class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0  # This is the index where next valid element will be placed

        for num in nums:
            # Always keep first two elements,
            # or if current num is not same as nums[k-2]
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
        
        return k
