#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    for i in range(len(roman_string)):
        current_val = roman_dict.get(roman_string[i], 0)
        
        # Əgər növbəti simvol varsa və indiki ondan kiçikdirsə
        if i + 1 < len(roman_string) and \
           current_val < roman_dict.get(roman_string[i + 1], 0):
            total -= current_val
        else:
            total += current_val
            
    return total
