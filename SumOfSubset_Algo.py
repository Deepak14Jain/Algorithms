def find(subset,n,sum,sol,ss):
    if sum == 0:
        sol = sol.append(ss)
        return
    if n == 0:
        return
    if subset[n-1] <= sum:
        find(subset,n-1,sum-subset[n-1],sol,ss+str(subset[n-1])+" ")
        find(subset,n-1,sum,sol,ss)
    else:
        find(subset,n-1,sum,sol,ss)
    
subset = input("Enter the subset elements:").split()
subset = [int(x) for x in subset]   # Stores the elements of the given set
subset.sort(reverse=True)   # Sort is done in reverse manner because we start from end
sum = int(input("Enter the sum value:"))
sol = list()    # List of all available solutions
ss = "" # string to store single solution subset
find(subset,len(subset),sum,sol,ss)
print(sol)