n = int(input("Enter the size of matrix:"))
print("Enter the adjacncy matrix with boolean values:")
mat = list()
for i in range(n):
    l = list()
    for j in range(n):
        l.append(int(input()))
    mat.append(l)
print("The adjacency matrix is:")
for i in mat:
    print(i)
sol = mat
k = 0
while(k<n):
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 or (mat[i][k]+mat[k][j] == 2):
                sol[i][j] = 1
    k += 1
    mat = sol
print("****Transitive Closure****")
for i in mat:
    print(i)