class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    result = len(blocks) + 1
    l = 0
    r = 0
    count = 0
    while r< len(blocks):
      if blocks[r] == 'W':
        count += 1
      if r - l + 1 == k:
        result = min(result , count)
        if blocks[l] == 'W':
        count -= 1
        l += 1
      r += 1
    return result