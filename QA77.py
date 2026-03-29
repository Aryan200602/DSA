#Remove brackets from an algebraic expression

def remove_brackets(s):
    result=""

    for ch in s:
        if ch!='(' and ch!=')':
            result+=ch

    return result

if __name__ == "__main__":
    expression = "3*(x+2) - (y-5)"
    print(remove_brackets(expression))
