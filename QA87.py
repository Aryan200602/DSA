#Shift the characters ascii by 1. 

def change(s):
    result=""

    for ch in s:
        if ch=='z':
            result+='a'
        elif ch=='Z':
            result+='A'

        result+=chr(ord(ch)+1)

    return result

if __name__ == "__main__":
    s = "Hello World"
    print(change(s))