class Solution {
  private void solve(char[][]grid , int i ,  int j){
    if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0'){
      return ;
    }

    grid[i][j] = '0';
    solve(grid , i + 1 , j );
    solve(grid , i - 1 , j );
    solve(grid , i  , j + 1 );
    solve(grid , i  , j - 1 );
  }
  public int numIslands(char[][] grid) {
    int result = 0;
    for(int i = 0 ; i < grid.length ; i++){
      for(int j = 0 ; j < grid[i].length; j++){
        if(grid[i][j] == '1'){
          result++;
          solve(grid , i , j);
        }
      }
    }
    return result;
  }
}