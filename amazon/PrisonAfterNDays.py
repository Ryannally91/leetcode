# leetcode solution

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        while N > 0:
            # we only need to run the fast-forward once at most
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N 
                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N

            # check if there is still some steps remained,
            # with or without the fast-forwarding.
            if N > 0:
                N -= 1
                next_day_cells = self.nextDay(cells)
                cells = next_day_cells

        return cells


    def nextDay(self, cells: List[int]):
        ret = [0]      # head
        for i in range(1, len(cells)-1):
            ret.append(int(cells[i-1] == cells[i+1]))
        ret.append(0)  # tail
        return ret


#### my solution
def prisonCells(cells, n):
    while n > 0:
        new_cell =[1] * len(cells)
        if cells[0] == 0:
            new_cell[0] = 1
        else:
            new_cell[0] = 0
        
        if cells[-1] == 0:
            new_cell[-1] = 1
        else:
            new_cell[0] = 0
            
        for i in range(1, len(cells)-2):
            if cells[i-1] == cells[i+1]:
                if cells[i] == 0:
                    new_cell[i] = 1
                else:
                    new_cell[i] = 0
        n -= 1
    print(new_cell)
    return new_cell
        
prisonCells([0,1,0,1,1,0,0,1], 7)
# [0,1,0,1,1,0,0,1]
# 7

# Expected
# [0,0,1,1,0,0,0,0]