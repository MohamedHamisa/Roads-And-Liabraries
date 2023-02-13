import collections

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib * n
    adj = collections.defaultdict(list)
    for start, des in cities:
        adj[start].append(des)
        adj[des].append(start)
    components = 0
    def dfs(city, visited):
        if city in visited:
            return 
        visited.add(city)
        for nei in adj.get(city,[]):
            dfs(nei, visited) 
    visited = set() 
    for i in range(1,n+1):
        if i not in visited:
            components += 1
            dfs(i, visited)
    res = ((n-components) * c_road) + (c_lib * components) 
    return res 
