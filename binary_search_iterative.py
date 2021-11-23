## Binary Search
def binary_search(a, key):
    # a is a sorted list of integers
    # key is the number to search in the list
    lo = 0
    hi = len(a)-1
    while lo <= hi:
        mid = int((lo + hi)/2)
        if key < a[mid]: 
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else: return mid
    return -1


a = [1,2,4,5,6]
print(binary_search(a, 30))