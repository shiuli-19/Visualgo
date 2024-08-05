import time  # Make sure to import the time module

def quick_sort(arr, drawrectangle, delay):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                drawrectangle(arr, ['blue' if x == i or x == j else 'red' for x in range(len(arr))])
                time.sleep(delay)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        drawrectangle(arr, ['blue' if x == i + 1 or x == high else 'red' for x in range(len(arr))])
        time.sleep(delay)
        return i + 1
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    drawrectangle(arr, ['blue' for x in range(len(arr))])

