class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        d = defaultdict(list)
        visited = set()
        result = 0
        def solve(start):
            q = deque([start])
            while q:
                city = q.popleft()
                for j in d[city]:
                    if j not in visited :
                        visited.add(j)
                        q.append(j)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    d[i].append(j)


        for i in range(len(isConnected)):
            if i not in visited:
                result += 1
                solve(i)
        return result



