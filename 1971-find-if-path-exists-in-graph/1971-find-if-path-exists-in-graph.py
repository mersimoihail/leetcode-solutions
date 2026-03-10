class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mydict = defaultdict(list)
        for vi,ui in edges:
            mydict[vi].append(ui)
            mydict[ui].append(vi)
        visite = set()
        def nodes(nod):
            if nod == destination:
                return True
            
            visite.add(nod)
            for neighbour in mydict[nod]:
                
                if neighbour not in visite:
                    if nodes(neighbour):
                        return True
            return False
        return nodes(source)
        
        
        



        

       
