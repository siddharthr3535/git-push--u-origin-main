import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
  public int minMeetingRooms(int[][] intervals) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    Arrays.sort(intervals, (a,b) -> a[0]-b[0]);

    for(int i = 0 ; i < intervals.length ; i++){
      if(!minHeap.isEmpty() && minHeap.peek() <= intervals[i][0]){
        minHeap.poll();
      }

      minHeap.add(intervals[i][1]);

    }

    return minHeap.size();
  }
}