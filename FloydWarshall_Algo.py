""" Floyd Warshall algorithm to determine minimum cost to reach a 
given node from one node either directly or via another node"""

n = int(input("Enter the number of vertices:"))
# making of cost martrix
cost = list()
print("Enter the cost matrix:")
for i in range(n):
    l = list()
    for j in range(n):
        l.append(int(input()))
    cost.append(l)
# Duplicate matrix creation == sol
sol = cost
k = 0
while(k<n):
    for i in range(n):
        for j in range(n):
            if i != j:
                # Floyd Warshall formula
                sol[i][j] = min(cost[i][j],(cost[i][k]+cost[k][j]))
    cost = sol
    k+=1
# Printing Solution
print("****Floyd Warshall****")
for i in sol:
    print(i)