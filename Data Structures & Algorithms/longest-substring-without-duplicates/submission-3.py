class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Sliding window

        # within the sliding window we use a hashmap

        # store value, and last seen index
        d = {}

        l = 0
        ans = 0

        for r in range(len(s)):
            
            #if invalid shrink window, use map to update in O(1)
            if s[r] in d and d[s[r]] >= l:

                # value after last seen value of r will be the new left
                l = d[s[r]] + 1
            
            # update new seen value to map
            d[s[r]] = r
            # update ans with current valid size
            
            ans = max(ans, r-l+1)

        return ans

        