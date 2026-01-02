"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, emp: List['Employee'], id: int) -> int:
        imp = {}
        sub = defaultdict(list)
        for i in range(len(emp)):
            imp[emp[i].id] = emp[i].importance
            for j in emp[i].subordinates:
                sub[emp[i].id].append(j)
        
        visited = set()
        result = 0

        def solve(id):
            if id not in visited:
                visited.add(id)
                nonlocal result
                result += imp[id]
                for i in sub[id]:
                    if i not in visited:
                        solve(i)
        solve(id)
        return result
            
