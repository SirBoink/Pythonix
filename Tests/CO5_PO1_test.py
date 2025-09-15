def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    while lo <= hi:
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1

def test_find_first_in_sorted():
    # Test case 1: Find first occurrence of 5 in array with duplicates
    result = find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 5)
    assert result == 2, f"Expected 2, got {result}"
    
    # Test case 2: Search for element not in array (too large)
    result = find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 7)
    assert result == -1, f"Expected -1, got {result}"
    
    # Test case 3: Search for element not in array (too small)
    result = find_first_in_sorted([3, 4, 5, 5, 5, 5, 6], 2)
    assert result == -1, f"Expected -1, got {result}"
    
    # Test case 4: Find element at end of array
    result = find_first_in_sorted([3, 6, 7, 9, 9, 10, 14, 27], 14)
    assert result == 6, f"Expected 6, got {result}"
    
    # Test case 5: Search for element not in array (middle range)
    result = find_first_in_sorted([0, 1, 6, 8, 13, 14, 67, 128], 80)
    assert result == -1, f"Expected -1, got {result}"
    
    # Test case 6: Find element in middle of array
    result = find_first_in_sorted([0, 1, 6, 8, 13, 14, 67, 128], 67)
    assert result == 6, f"Expected 6, got {result}"
    
    # Test case 7: Find last element in array
    result = find_first_in_sorted([0, 1, 6, 8, 13, 14, 67, 128], 128)
    assert result == 7, f"Expected 7, got {result}"
    
    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_find_first_in_sorted()
