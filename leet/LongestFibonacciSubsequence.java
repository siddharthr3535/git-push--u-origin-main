import java.util.HashSet;
import java.util.Set;

class Solution {
  public int lenLongestFibSubseq(int[] arr) {
    Set<Integer> set = new HashSet<>();
    for(int i : arr){
      set.add(i);
    }
    int result = 0;
    for(int i = 0 ; i < arr.length - 1; i++){
      for(int j = i + 1 ; j < arr.length ;j++){
        int prev = arr[i] ;
        int current = arr[j];
        int next = prev + current;
        int length = 2;
        while(set.contains(next)){
          length++;
          prev = current;
          current = next;
          next = prev + current;
          result = Math.max(result , length);
        }
      }
    }
    return result;
  }
}


