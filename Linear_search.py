def linear_search(arr, target):
    """
    Perform linear search to find the target element in the given array.

    Parameters:
        arr (list): The list to search through.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target found
    return -1  # Return -1 if target not found


# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
target = 5
result = linear_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")
