import time  # Ensure time module is imported

def selection_sort(arr, drawrectangle, delay):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        drawrectangle(arr, ['blue' if x == i or x == min_idx else 'red' for x in range(len(arr))])
        time.sleep(delay)
    drawrectangle(arr, ['blue' for x in range(len(arr))])
