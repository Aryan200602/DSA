#remove all characters from a string except alphabets

def keep_alphabets(s):
    result = ""
    
    for c in s:
        if c.isalpha():   # checks if character is a letter
            result += c
            
    return result


# Example
s = "H3llo W@rld! 123"
print(keep_alphabets(s))