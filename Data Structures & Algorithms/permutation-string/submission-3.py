class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        

        # build frequency map of s1
        freq_s1 = Counter(s1)

        # sliding window
        l = 0

        # currentwindow -> hashmap -> (letter, count)
        curr_win = {}

        # right pointer moves (valid) -> the current window is a subset of s1
        for r in range(len(s2)):
            
            # add to map
            curr_win[s2[r]] = curr_win.get(s2[r], 0) + 1

            # while (invalid) -> current window is not a subset
            while l < r and curr_win.get(s2[l], 0) > freq_s1.get(s2[l],0):
                #decrease when moved out the window
                curr_win[s2[l]] = curr_win.get(s2[l]) - 1
                if curr_win[s2[l]] == 0:
                    del curr_win[s2[l]]
                l += 1

            #if s1 and window is same -> return True
            if curr_win.items() == freq_s1.items():
                return True

        return False