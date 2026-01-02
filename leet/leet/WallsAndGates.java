import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solution {
  private void solve(int[][] rooms, int i, int j, Set<String> visited, Queue<int[]> q) {
    if (i < 0 || j < 0 || i >= rooms.length || j >= rooms[0].length || rooms[i][j] == -1 || visited.contains(i + "," + j)) {
      return;
    }
    visited.add(i + "," + j);
    q.add(new int[]{i, j});
  }

  public void wallsAndGates(int[][] rooms) {
    Queue<int[]> q = new LinkedList<>();
    Set<String> visited = new HashSet<>();

    for (int i = 0; i < rooms.length; i++) {
      for (int j = 0; j < rooms[i].length; j++) {
        if (rooms[i][j] == 0) {
          q.add(new int[]{i, j});
          visited.add(i + "," + j);
        }
      }
    }

    int distance = 0;
    while (!q.isEmpty()) {
      int size = q.size();
      for (int k = 0; k < size; k++) {
        int[] cell = q.remove();
        int i = cell[0], j = cell[1];
        rooms[i][j] = distance;

        solve(rooms, i + 1, j, visited, q);
        solve(rooms, i - 1, j, visited, q);
        solve(rooms, i, j + 1, visited, q);
        solve(rooms, i, j - 1, visited, q);
      }
      distance++;
    }
  }
}
