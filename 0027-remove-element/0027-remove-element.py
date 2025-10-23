class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # The Pointer to place the next non-val element

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k
