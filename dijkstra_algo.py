my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}
def dijkstra_algo(graph,start,target=''):
    d={key:0 if key==start else float('inf') for key in graph }
    unvisited=list(graph)
    while unvisited:#same as while unvisited!=[]:
        current=min(unvisited,key=d.get)
        for node,edge in graph[current]:
            if d[current]+edge<d[node]:
                d[node]=d[current]+edge
        unvisited.remove(current)
    targets=[target] if target else d
    for node in targets:
        if node==start:
            continue
        print(f'\n{start}-{node} distance: {d[node]}')
dijkstra_algo(my_graph,'A',target='')