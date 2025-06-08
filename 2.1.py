def find_unique_elements(lst):
    # Dictionary to store the count of each element
    count_dict = {}
    
    # Counting occurrences of each element
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # List to store unique elements
    unique_elements = []
    
    # Adding unique elements to the list
    for num, count in count_dict.items():
        if count == 1:
            unique_elements.append(num)
    
    return unique_elements

# Example usage
input_list = [3, 6, 9, 2, 3, 9, 1, 15, 21, 3, 1]
unique_elements = find_unique_elements(input_list)
print("Original List:", input_list)
print("Unique elements:", unique_elements)
