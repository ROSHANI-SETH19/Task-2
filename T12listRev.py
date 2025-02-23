def reverse_list(input_list):
    left = 0
    right = len(input_list) - 1
    
    while left < right:
        # Swap elements
        input_list[left], input_list[right] = input_list[right], input_list[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    return input_list

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Reversed list:", reverse_list(numbers))