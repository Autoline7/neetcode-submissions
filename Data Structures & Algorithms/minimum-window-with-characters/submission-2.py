class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        ans = ["", 100000]
        # hashmap1 -> (char, count) -> freq of t
        dic1 = {}

        for c in t:
            dic1[c] = dic1.get(c,0) + 1

        # hashmap2 -> (char, count) -> track the current window freq
        dic2 = {}


        #count valid chars with their count that are in both maps
        count = 0

        # iterate right pointer until reaches the end
        for r in range(len(s)):
            
            dic2[s[r]] = dic2.get(s[r],0) + 1

            if s[r] in dic1 and dic1[s[r]] == dic2[s[r]]:
                count += 1

            #shrink while valid -> when hashmap1 is a subset of hashmap2
            while count == len(dic1):
                if r-l+1 <= ans[1]:
                    ans[0] = s[l:r+1]
                    ans[1] = r-l+1
                
                dic2[s[l]] -= 1
                if s[l] in dic1 and dic1[s[l]] > dic2[s[l]]:
                    count -= 1

                l += 1
            
        return ans[0]