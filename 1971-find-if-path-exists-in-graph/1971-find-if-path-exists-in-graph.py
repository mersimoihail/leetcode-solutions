class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for vi,ui in edges:
            dic[vi].append(ui)
            dic[ui].append(vi)
        
        visited = set()
        def traver(nod):
            if nod == destination:
                return True
            visited.add(nod)
            for i in dic[nod]:
                if i not in visited:
                    if traver(i):
                        return True
            return False
        
        return traver(source)
            

        
        