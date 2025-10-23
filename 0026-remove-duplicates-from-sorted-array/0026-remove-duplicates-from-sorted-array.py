class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # This one is the Pointer for the last unique element
        i = 0
        
        # The Loop through the array starting from the 2nd element is
        for j in range(1, len(nums)):
            # When a new unique element is found
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # Return number of unique elements as (index + 1)
        return i + 1
