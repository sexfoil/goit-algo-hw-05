def binary_search(array, target):
    left, right = 0, len(array) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if array[mid] == target:
            return iterations, array[mid]
        elif array[mid] < target:
            left = mid + 1
        else:
            upper_bound = array[mid]
            right = mid - 1
    
    return iterations, upper_bound


sorted_array = [0.1, 0.5, 1.2, 2.4, 3.7, 4.8, 5.9, 7.3, 8.0, 8.8, 9.1, 9.6]

print(binary_search(sorted_array, 2.50)) # має бути (4, 3.7)
print(binary_search(sorted_array, 1.20)) # має бути (2, 1.2)
