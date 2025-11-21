import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
  public int[] rearrangeBarcodes(int[] barcodes) {
    Map<Integer, Integer> map = new HashMap<>();
    for(int i : barcodes){
      map.put(i, map.getOrDefault(i, 0) + 1);
    }
    PriorityQueue<Integer> maxheap = new PriorityQueue<>((a,b)-> map.get(b) - map.get(a));
    int [] result = new int[barcodes.length];
    int index = 0;
    maxheap.addAll(map.keySet());
    while(!maxheap.isEmpty()){
      int first = maxheap.poll();
      int second = maxheap.isEmpty() ? - 1 : maxheap.poll();
      map.put(first , map.get(first) - 1);
      result[index++] = first;
      if(second != -1){
        result[index++] = second;
        map.put(second , map.get(second) - 1);

      }
      if (map.get(first) > 0){
        maxheap.offer(first);
      }
      if(second != -1){
        if(map.get(second) > 0){
          maxheap.offer(second);
        }
      }
    }

    return result;
  }
}