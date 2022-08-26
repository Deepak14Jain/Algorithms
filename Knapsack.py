"""Knapsack problem is used to find a subset of given items
that has maximum profit within the given knapsack weight"""

n = int(input("Enter the number of items:"))
# Profit list starting with index 0
p = input("Enter profit of all items:").split()
p = [int(x) for x in p]
# Weight list starting with index 0
w = input("Enter weight of all items:").split()
w = [int(x) for x in w]
# The Knapsack weight
W = int(input("Enter Knapsak weight:"))
# Knapsack table starting with index 1
mat = [[0 for j in range(W+1)]for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,W+1):
        if j-w[i-1] < 0:
            mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = max(mat[i-1][j],(mat[i-1][j-w[i-1]]+p[i-1]))
print(mat)