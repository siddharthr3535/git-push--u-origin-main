class Solution {


  private int solve(int[][] grid, int i, int j) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == 0) {
      return 0;
    }
    grid[i][j] = 0;
    return 1 + solve(grid, i + 1, j) + solve(grid, i - 1, j) + solve(grid, i, j + 1) + solve(grid, i, j - 1);
  }

  public int maxAreaOfIsland(int[][] grid) {
    int result = 0;
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[i].length; j++) {

        if (grid[i][j] == 1) {
          result = Math.max(result , solve(grid, i, j));
        }
      }
    }
    return result;
  }
}