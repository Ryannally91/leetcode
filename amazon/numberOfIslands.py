#approach using tree stucture  
#DFS
def numIslands(grid):
    count = 0

    directions=[(1,0), (-1, 0), (0,1), (0, -1)]

    def set_island_0(grid, r, c):  #this modifies the original input, if not allowed then create dict to track where you've already visited
        if(0<= r < len(grid) and ( 0 <= c < len(grid))) and grid[r][c] == '1':
            grid[r][c] = '0'

            for row_inc, col_inc in directions:
                set_island_0(grid, r + row_inc, c + col_inc)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                count += 1

                set_island_0(grid, row, col)
    return count            
             



