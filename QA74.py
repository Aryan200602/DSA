#remove all the spaces from a string

def removeWhitespaces(s):
        result = ""
        
        
        for c in s:
            
            if c != ' ' and c != '\t' and c != '\n':
                result += c
        return result

if __name__ == "__main__":
    input_str = "  Hello   World! This is   Python  "

    output =removeWhitespaces(input_str)

    print(output)
