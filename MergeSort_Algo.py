def sort(arr, first, last):
    if(first<last):
        mid = (first+last)//2
        sort(arr, first, mid)
        sort(arr, mid+1, last)
        merge(arr, first, mid, last)

def merge(arr, first, mid, last):
    left = arr[first:mid+1]
    right = arr[mid+1:last+1]
    i=0
    j=0
    k=first
    while(i<len(left) and j<len(right)):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while(i<len(left)):
        arr[k] = left[i]
        i+=1
        k+=1
    while(j<len(right)):
        arr[k] = right[j]
        j+=1
        k+=1

arr = input("Enter the list of numbers:").split()
arr = [int(x) for x in arr]
sort(arr,0,len(arr)-1)
print(arr)