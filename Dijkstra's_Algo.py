"""Dijkstra's algorithm is used to find minimum cost 
from source node to all other nodes"""

def dij(n,v,cost,dijs):
    for i in range(n):
        if (dijs[v] + cost[v][i]) < dijs[i]:
            dijs[i] = dijs[v] + cost[v][i]
            dij(n,i,cost,dijs)

n = int(input("Enter number of nodes:"))
cost = [[0 for j in range(n)]for i in range(n)]
print("Enter the adjacency matrix:")
for i in range(n):
    for j in range(n):
        temp = int(input())
        if temp == 0:
            cost[i][j] = 999    # 999/0 implies no path exists
        else:
            cost[i][j] = temp
            
v = int(input("Enter the source node:"))
dijs = [999 for i in range(n)]  # list to store minimum cost of reaching every other node from source node
dijs[v] = 0 # Cost of reaching source node is by default zero
dij(n,v,cost,dijs)
# Printing Output
for i in range(n):
    if i!=v:
        print("{} ----> {}  MinCost:{}".format(v,i,dijs[i]))
