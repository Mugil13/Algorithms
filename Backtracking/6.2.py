def remove_invalid_parentheses(s: str) -> list[str]:
    left_remove_count, right_remove_count = 0, 0
    for char in s:  
        left_remove_count += (char == '(')
        if left_remove_count == 0:
            right_remove_count += (char == ')')
        else:
            left_remove_count -= (char == ')')
    
    # Function to check if the string is in a valid form
    def is_valid(string):
        count = 0
        for char in string:
            if char == '(': 
                count += 1
            if char == ')': 
                count -= 1
            if count < 0: 
                return False
        return count == 0
    
    # Backtracking DFS function 
    def dfs_backtracking(combination, start, left, right):
        current_str = ''.join(combination)
        
        if left == 0 and right == 0 and is_valid(current_str): 
            results.append(current_str)
            return
        
        for i in range(start, len(s)):
            if s[i] != '(' and s[i] != ')': 
                continue
            if i != start and s[i] == s[i - 1]: 
                continue
            
            # Remove invalid ")" before "(" 
            if right > 0 and s[i] == ')':
                combination[i] = '' 
                dfs_backtracking(combination, i + 1, left, right - 1)
                combination[i] = s[i]  
            elif left > 0 and s[i] == '(':
                combination[i] = '' 
                dfs_backtracking(combination, i + 1, left - 1, right)
                combination[i] = s[i] 
    
    results = []
    dfs_backtracking(list(s), 0, left_remove_count, right_remove_count)
    
    return results

s = input("Enter a string with parentheses: ")
result = remove_invalid_parentheses(s)
if result:
    print("Valid combinations after removing invalid parentheses:")
    for res in result:
        print(res)
else:
    print("No valid combinations exist after removing invalid parentheses.")
