class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        q = deque()
        start = tuple(nums1)
        target = tuple(nums2)
        if nums1 == nums2:
            return 0
        q.append((start, 0))
        if sorted(nums1) != sorted(nums2):
            return -1
        visited = set()
        visited.add(start)
        while q:
            state , count = q.popleft()
            n = len(state)
            for i in range(n):
                for j in range(i, n):
                    sub = state[i:j+1]
                    rem = state[:i] + state[j+1:]
                    for k in range(len(rem) + 1):
                        changed = rem[:k+1] + sub + rem[k+1:]
                        if changed == target:
                            return count + 1
                        if changed not in visited:
                            visited.add(changed)
                            q.append((changed, count + 1))
        return -1