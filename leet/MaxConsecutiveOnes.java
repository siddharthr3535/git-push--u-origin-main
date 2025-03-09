class Solution {
  public int longestOnes(int[] nums, int k) {
    int i = 0, j = 0;
    int result = 0;
    int n = nums.length;
    int count = 0;
    while (j < n) {
      if(nums[j] == 0){
        count++;
      }
      if(count > k){
        result = Math.max(result , j - i );
        while(count > k){
          if(nums[i] == 0){
            count--;
          }
          i++;
        }
      }
      j++;
    }
    if(count <=k){
      result = Math.max(result , j - i);
    }
    return result;
  }
}