class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window

        # the current window -> set to determine dups in O(1)
        seen = {}
        ans = 0
        l = 0

        # iterating
        for r in range(len(s)):
            
            # dec window when -> curr val is a dup and we keep inc left pointer until we pass the cup (future improvement is to use a map to skip to that index faster)
            # only update if when r is withing in window

            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            
            # inc window when -> curr val is not a dup
            seen[s[r]] = r
            ans = max(ans, r-l+1)

        return ans

        