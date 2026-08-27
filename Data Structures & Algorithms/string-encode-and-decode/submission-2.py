class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        
        # "12#adasondpaosd4#asdg6#asddea"
        # O(n)
        print("".join(parts))
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            # capture number (values until you hit the "#")
            num = []
            while s[i] != '#':
                num.append(s[i])
                i += 1
            
            length = int("".join(num))
            i += 1
            # get the substring (size of the number above for the word) and add to ans
            # 5#Hello5#World
            # i = 2 ("H")

            # new i = 8 ("3")
            ans.append(s[i: i + length])
            # update i 
            i += length
        
        return ans
            





