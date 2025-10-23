class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers can't be palindromes
        if x < 0:
            return False
        
        # Convert to string and compare with its reverse
        s = str(x)
        return s == s[::-1]
