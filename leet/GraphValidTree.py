class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()
        d = defaultdict(list)

        def solve(i):
            q = deque([(i, -1)])

            while q:
                # print(q)
                node, parent = q.popleft()
                visited.add(node)
                # print(q)
                for j in d[node]:
                    if j not in visited:
                        # visited.add(node)
                        q.append((j,node))
                    else:
                        if j != parent:
                            return True
            return False


        for i, j in edges:
            d[i].append(j)
            d[j].append(i)


        if solve(0):
            return False


        return len(visited) == n
