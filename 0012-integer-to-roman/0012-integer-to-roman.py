class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of Roman symbols and their values (in descending order)
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        # Go through each value-symbol pair
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman += symbols[i]

        return roman
