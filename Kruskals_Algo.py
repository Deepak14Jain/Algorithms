"""Kruskal's algorithm is used to determine minimum spanning tree
by recursively adding edges with given weights in ascending order
and also making sure no cycles are formed and all the vertices are included"""

# find() and union() function take care of eliminating cycles
def find(i):
	while parent[i] != i:
		i = parent[i]
	return i

def union(i, j):
	a = find(i)
	b = find(j)
	parent[a] = b

def kruskalMST(cost):
	mincost = 0 
	edge_count = 0
	while edge_count < V - 1:
		min = 999
		a = -1
		b = -1
		for i in range(V):
			for j in range(V):
				if find(i) != find(j) and cost[i][j] < min:
					min = cost[i][j]
					a = i
					b = j
		union(a, b)
		print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
		edge_count += 1
		mincost += min
	print("Minimum cost= {}".format(mincost))

V = int(input("Enter the number of vertices:"))
parent = [i for i in range(V)]
print("Enter the cost matrix:")
cost = list()
for i in range(V):
    l = list()
    for j in range(V):
        temp = int(input())
        if temp == 0:
            l.append(999)
        else:
            l.append(temp)
    cost.append(l)
kruskalMST(cost)
