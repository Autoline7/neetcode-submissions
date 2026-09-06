class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # to count the differences

        # once the difference count is reached 
        # count_diff will be called which counts the diff for that step
        # it will use a hashmap with the count of each of the values in that window

        # maybe there's a way to keep knowledge of the highest count? heap?


        l = 0
        ans = 0
        d = {}

        for r in range(len(s)):
            
            # value -> (index, count)
            d[s[r]] = (r,d.get(s[r], ('',0))[1]+1)
            
            # if invalid
            
                # iterate throiugh the map and find the max_count
                    # at each step we keep track of the total and the max_individual
            total = 0
            max_individual = 0
            for key, value in d.items():
                total += value[1]
                max_individual = max(max_individual, value[1])

            # subtract max_individual and total to get the diffrence count
            diff_count = total - max_individual
            # if the diff_count is > k then we update the l by 1
            if diff_count > k:
                d[s[l]] = (s[l], d.get(s[l], ('',0))[1] - 1)
                l += 1

            # update ans
            ans = max(ans, r-l+1)
        
        return ans

