"""Topological sorting is a way of getting nodes of the graph
based on the condition that the node has an inorder equals to zero"""

n = int(input("Enter the number of vertices:"))
graph = list()
print("Enter adjacency matrix of the graph:")
for i in range(n):
    l = list()
    for j in range(n):
        l.append(int(input()))
    graph.append(l)
arr = list()
i = 0
while(len(arr) != n):
    free = True
    for j in range(n):
        if graph[j][i] == 1:
            free = False
    if free and (i not in arr):
        arr.append(i)
        for k in range(n):
            graph[i][k] = 0
    i = (i+1)%n
# Output array
print("The solution array is:",arr)