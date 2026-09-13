class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window

        # the current window -> set to determine dups in O(1)
        seen = set()
        ans = 0
        l = 0

        # iterating
        for r in range(len(s)):
            
            # dec window when -> curr val is a dup and we keep inc left pointer until we pass the cup (future improvement is to use a map to skip to that index faster)

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # inc window when -> curr val is not a dup
            seen.add(s[r])
            ans = max(ans, r-l+1)

        return ans

        