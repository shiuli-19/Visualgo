import time
def merge_sort(data, drawrectangle, delay):
    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort_helper(L)
            merge_sort_helper(R)
            merge(L, R, arr)

    def merge(L, R, arr):
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        drawrectangle(arr, ['blue' if x < len(L) else 'red' for x in range(len(arr))])
        time.sleep(delay)

    merge_sort_helper(data)
    drawrectangle(data, ['blue' for x in range(len(data))])

