from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        prefix_top_sum = [0]*cols
        prefix_bottom_sum = [0]*cols
        # populate prefix sum for top row and bottom row
        for i in range(1, cols):
            prefix_top_sum[i] = grid[0][i-1] + grid[0][i]
            prefix_bottom_sum[i] = grid[1][i-1] + grid[1][i]

        min_second_robot_score = float('inf')

        for i in range(cols):
            top_sum = prefix_top_sum[-1] - grid[0][i]
            bottom_sum = prefix_bottom_sum[i-1] if i > 0 else 0

            robot2_points = max(top_sum, bottom_sum)
            min_second_robot_score = min(robot2_points, min_second_robot_score)
        
        return min_second_robot_score

grid = [[2,5,4],[1,5,1]]
print(Solution().gridGame(grid))