class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic1 = {}

        for i in range(len(s)):
            dic1[s[i]] = dic1.get(s[i], 0) + 1

        for i in range(len(t)):
            dic1[t[i]] = dic1.get(t[i], 0) - 1

        for key in dic1:
            if dic1.get(key) != 0:
                return False

        return True


            