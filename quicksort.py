def partition(A, p, q):
    x = A[p]
    i = p
    
    // watch the range
    for j in range(p+1, q+1): 
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            
    temp1 = A[p]
    A[p] = A[i]
    A[i] = temp1

    return i

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

A = [6,10,13,5,8,3,2,11]
quicksort(A, 0, 7)
print A
