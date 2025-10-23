class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])          # Each word has same length
        word_count = len(words)           # Total number of words
        total_len = word_len * word_count # Total length of concatenated substring

        # Frequency map of all words
        word_map = {}
        for w in words:
            word_map[w] = word_map.get(w, 0) + 1

        result = []

        # Check for every possible starting position (offsets)
        for i in range(word_len):
            left = i
            curr_map = {}
            count = 0

            # Move window in chunks of word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_map:
                    curr_map[word] = curr_map.get(word, 0) + 1
                    count += 1

                    # If word appears too many times, shrink from the left
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If window contains all words → record index
                    if count == word_count:
                        result.append(left)

                        # Slide window forward by one word
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # Reset window when invalid word found
                    curr_map.clear()
                    count = 0
                    left = j + word_len

        return result
