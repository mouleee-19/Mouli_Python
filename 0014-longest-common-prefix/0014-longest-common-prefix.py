class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Take the first word as a starting prefix
        prefix = strs[0]

        # Compare prefix with each word
        for s in strs[1:]:
            # Trim the prefix until it matches the start of the current word
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""  # No common prefix

        return prefix
