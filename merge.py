import concurrent.futures

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        left_future = executor.submit(merge_sort, left)
        right_future = executor.submit(merge_sort, right)
        left = left_future.result()
        right = right_future.result()
    
    return merge(left, right)

# Datos de ejemplo
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = merge_sort(data)
print("Datos ordenados:", sorted_data)
