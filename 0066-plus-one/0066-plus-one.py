class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            # If current digit is less than 9, simply add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set to 0 and continue carry to next digit
            digits[i] = 0
        
        # If all digits were 9, we need an extra 1 at the front
        return [1] + digits
