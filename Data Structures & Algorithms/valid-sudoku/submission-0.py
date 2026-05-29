class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check 3x3 grids
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                valid = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in valid:
                            return False

                        valid.add(val)

        # Check rows
        for r in range(9):
            valid = set()

            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in valid:
                    return False

                valid.add(val)

        # Check columns
        for c in range(9):
            valid = set()

            for r in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in valid:
                    return False

                valid.add(val)

        return True