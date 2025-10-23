class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i, n = 0, len(s)
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1

        # Step 3: Read digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Step 4: Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1

        return sign * result
