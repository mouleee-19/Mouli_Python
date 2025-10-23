class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0                      # This is start pointer
        right = len(height) - 1       # This is end pointer
        max_area = 0

        while left < right:
            # Now Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = h * width
            max_area = max(max_area, area)

            # Move the pointer pointing to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
