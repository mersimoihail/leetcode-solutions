class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adlist = [[] for _ in range(n)]

        

        for i in range(len(edges)):
            adlist[edges[i][0]].append(edges[i][1])
            adlist[edges[i][1]].append(edges[i][0])
        visited = set()
        def dfs(vertix):
            if vertix == destination:
                return True
            visited.add(vertix)
            for neighbour in adlist[vertix]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)

