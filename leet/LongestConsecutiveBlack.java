class Solution {
  public int minimumRecolors(String blocks, int k) {
    int result = Integer.MAX_VALUE;

    for(int i = 0 ; i <= blocks.length() - k ; i ++){
      int count = 0;
      // System.out.println(i);
      for(int j = i  ; j < i + k ; j++){

        if(blocks.charAt(j) == 'W'){
          count += 1;
        }
      }
      result= Math.min(result , count);
    }
    return result;
  }
}