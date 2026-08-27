class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = sorted word, value = word
        dic = {}


        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in dic:
                dic[sorted_word] = []
            dic[sorted_word].append(word)
        return list(dic.values())