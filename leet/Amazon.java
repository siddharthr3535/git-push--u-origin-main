class Pair {
  int first;
  int second;

  Pair(int first, int second) {
    this.first = first;
    this.second = second;
  }
}
public class LongestConsecutiveSequence {
  Stack<Pair> stack;
  Stack<Pair> stack2;
  int result;
  public LongestConsecutiveSequence() {
    stack = new Stack<>();
    stack2 = new Stack<>();
    result = 0;

  }

  // Adds the number and returns the length of the longest consecutive sequence so far
  public int addNumberAndCompute(int num) {
    if(stack.size() == 0){
      stack.append(new Pair(num , 1));
      return 1;
    }
    while(!stack.isEmpty() && stack.pop().first >= num - 1){
      stack2.add(stack.pop());
    }
    if(stack.peek().first == num - 1){
      stack.add(new Pair(num ,stack.peek().second + 1 ));
      result = Math.max(result ,stack.peek().second  );
    }
    else{
      stack.add(new Pair(num , 1 ));
    }
    while(!stack2.isEmpty()){
      stack.add(stack2.pop());
    }
    return result;
  }
}
