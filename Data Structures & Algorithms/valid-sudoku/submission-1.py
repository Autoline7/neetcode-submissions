class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows and columns are valid
        for i in range(9):
            rows_seen = set()
            cols_seen = set()
            for j in range(9):
                curr1 = board[i][j]
                curr2 = board[j][i]


                if curr1 != ".":
                    if curr1 in rows_seen:
                        return False
                    rows_seen.add(curr1)
                
                if curr2 != ".":
                    if curr2 in cols_seen:
                        return False
                    cols_seen.add(curr2)
        
        print("rows and columns are valid")

        # check if subboxes are valid

        for i in range(3):

            for j in range(3):
                seen = set()
                for k in range(3):

                    for l in range(3):
                        curr_c = (j * 3) + l
                        curr_r = (i * 3) + k

                        curr = board[curr_r][curr_c]

                        if curr != ".":
                            if curr in seen:
                                return False
                            seen.add(curr)
        
        print("suboxes are valid")
        return True





        