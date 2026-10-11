class Solution(object):
    def findSubstring(self, s, words):
        result = []
        word_len = len(words[0])
        total_len = word_len * len(words)

        for i in range(len(s) - total_len + 1):
            sub = s[i:i + total_len]
            temp = []

            for j in range(0, total_len, word_len):
                temp.append(sub[j:j + word_len])

            if sorted(temp) == sorted(words):
                result.append(i)

        return result


obj = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]

print(obj.findSubstring(s, words))