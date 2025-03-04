class Solution {
  private boolean result = false;
  private void solve(int[] arr , int n , int i, int current){
    if(i >= 17 || current > n){
      return ;
    }
    if(current == n){
      result = true;
      return ;
    }
    solve(arr, n, i + 1, current + arr[i]);
    solve(arr, n, i + 1, current);
  }
  public boolean checkPowersOfThree(int n) {
    int[] arr = new int[17];
    for(int i  = 0 ; i <= 16; i++){
      arr[i] = (int)Math.pow(3,i);
      if(arr[i] >= n){
        break;
      }
    }

    solve(arr , n , 0 , 0);
    return result;

  }
}