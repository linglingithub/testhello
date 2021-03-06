#coding=utf-8

import unittest

"""

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Depth-first Search Breadth-first Search Union Find
Hide Similar Problems (M) Surrounded Regions (M) Walls and Gates (H) Number of Islands II (M) Number of Connected
Components in an Undirected Graph

Medium

========================================================================================================================

Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we
consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Have you met this question in a real interview? Yes
Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.

Tags
Facebook Zenefits Google
Related Problems
Medium Surrounded Regions 21 %
Hard Number of Islands II


"""


class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        result = 0
        queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                    result += 1
                    self.dfs(grid, queue)

        return result

    def dfs(self, grid,queue):

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while queue:
            tmp = queue.pop(0)
            x, y = tmp[0], tmp[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    grid[nx][ny] = 0


class Solution1(object):
    def numIslands(self, grid): #159ms, 42%
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _x in range(n)] for _y in range(m)]
        self.island_cnt = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and int(grid[i][j]) == 1:
                    self.island_cnt += 1
                    self.traverse_island(grid, i, j, visited)
        return self.island_cnt

    def traverse_island(self, grid, x, y, visited):
        queue = [(x,y)]
        visited[x][y] = True
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while queue:
            cx, cy = queue.pop(0)
            for i in range(4):
                nx = cx+dx[i] # careful, not x, y here!!!
                ny = cy+dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]): # DO NOT forget to check boundery
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if int(grid[nx][ny]) == 1:
                            queue.append((nx,ny))









class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          [1, 1, 0, 0, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1]
        ]
        answer = 3
        result = self.sol.numIslands(nums)
        self.assertEqual(answer, result)

    def test_case02(self): #====> from leetcode, use str format
        nums = ["11110","11010","11000","00000"]
        answer = 1
        result = self.sol.numIslands(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
