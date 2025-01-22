# https://leetcode.com/problems/map-of-highest-peak/description/?envType=daily-question&envId=2025-01-22 
from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        # this is updated grid on which we will return 
        height = [[-1]*cols for _ in range(rows)]

        dq = deque()
        # iterate throught the grid to find the water cells and add it to queue 
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1: # if it's a water cell
                    dq.append((i, j)) # add this index into dq 
                    height[i][j] = 0 # make this cell 0 as asked in problem statment
        
        # Now run bfs 
        while dq:
            i, j = dq.popleft()

            # iterate in all 4 directions from the current cell 
            for di, dj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                # check if these cells are within the bound and -1 
                if 0 <= di < rows and 0 <= dj < cols and height[di][dj] == -1:
                    # update height grid by value by 1 
                    height[di][dj] = height[i][j] + 1
                    # add these idx to the queue
                    dq.append((di, dj))

        return height



isWater = [[0,1],[0,0]]

print(Solution().highestPeak(isWater))