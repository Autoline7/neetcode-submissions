class Solution:

    directions = [[-1,0], [1,0], [0,-1], [0,1]]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ans = []

        # iterate over rows
        for i in range(len(heights)):

            #iterate over columns
            for j in range(len(heights[0])):
                curr = heights[i][j]

                # reached when
                    # pacific: left most columns and upper row -> i = 0 or j = 0
                    # atlantic: right most columns and lower row -> i-1 = 0 pr j-1 = 0
                # at each index check if its possible to reach both oceans

                # use dfs -> pass in where the goal is, and returns boolean

                # if both are true add to ans

                seen1 = [[False] * len(heights[0]) for _ in range(len(heights))]
                seen2 = [[False] * len(heights[0]) for _ in range(len(heights))]
                paci = self.dfs(i, j, heights, "pac", seen1)
                atl = self.dfs(i, j, heights, "atl", seen2)

                if paci and atl:
                    ans.append([i,j])
            

        return ans

    def dfs(self, i, j, heights, ocean, seen):
        seen[i][j] = True
        if ocean == "pac":
            if i == 0 or j == 0:
                return True
        if ocean == "atl":
            if len(heights)-1 == i or len(heights[0])-1 == j:
                return True
            
        for direction in self.directions:
            nr = direction[0] + i
            nc = direction[1] + j

            if self.valid(nr,nc,heights) and not seen[nr][nc] and heights[i][j] >= heights[nr][nc]:
                if self.dfs(nr, nc, heights, ocean, seen):
                    return True
    

    def valid(self, i, j, heights):
        return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0]) 





