class Solution {
  private void solve(char[][]board , int i , int j ){
    if(i < 0 || i >= board.length  || j < 0 || j >= board[i].length ||board[i][j] == 'X' || board[i][j] == 'T'){
      return ;
    }
    board[i][j] = 'T';
    solve(board , i + 1 , j );
    solve(board , i - 1 , j );
    solve(board , i  , j + 1);
    solve(board , i  , j - 1 );

  }
  public void solve(char[][] board) {
    for(int i = 0 ; i < board.length ; i++){
      for(int j = 0 ; j < board[i].length ; j++){
        if(board[i][j] == 'O' && (i==0 ||i == board.length - 1 || j==0 || j == board[i].length - 1)){
          solve(board , i , j);
        }
      }
    }

    for(int i = 0 ; i < board.length ; i++){
      for(int j = 0 ; j < board[i].length ; j++){
        if(board[i][j] == 'O'){
          board[i][j] = 'X';
        }
      }
    }

    for(int i = 0 ; i < board.length ; i++){
      for(int j = 0 ; j < board[i].length ; j++){
        if(board[i][j] == 'T'){
          board[i][j] = 'O';
        }
      }
    }

  }
}