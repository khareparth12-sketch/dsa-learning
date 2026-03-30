def bubbleSort(arr):
    pass

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

n = list(map(int, input().split()))
arr_sorted = selectionSort(n)
print(arr_sorted)
