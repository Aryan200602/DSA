#print the repeating characters in a string

def rep(s):
    freq=[0]*256
    seen=[False]*256
    result=[]

    for ch in s:
        if not seen[ord(ch)]:
            seen[ord(ch)]=True 
        else:
            result.append(ch)

    return ''.join(result)

if __name__ == "__main__":
    s = "hello world"
    print(rep(s))

    