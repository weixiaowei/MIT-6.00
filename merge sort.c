def merge(left, right):
    """Assumes left and right are sorted lists.Returns a new sorted list
    containing the same elements as (left + right) would contain."""

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while (i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result


def mergeSort(L):
    """Returns a new sorted list with the same elements as L"""

    print L
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) / 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = merge(left,right)
        print 'merged', together
        return together

L = [1, 4, 6, 8, 4, 3, 9, 5, 0]
N = mergeSort(L)
print N

