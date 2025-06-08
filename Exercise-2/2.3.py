def most_frequent_letters(word):
    char_dict = {}
    
    # Count the occurrences of each character in the string
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    # Find the maximum frequency
    max_freq = max(char_dict.values())
    
    #Create a list to store the maximum frequency letters
    most_frequent_list = []

    for char, freq in char_dict.items():
        if freq == max_freq:
            most_frequent_list.append(char)

    return most_frequent_list

word = input("Enter a string: ")
frequency = most_frequent_letters(word)
print("List of most frequently occurring characters:", frequency)
