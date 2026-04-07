

def rem(s1,s2):

    seen=[False]*256
    result=[]

    for ch in s2:
        if not seen[ord(ch)]:
            seen[ord(ch)]=True 
    
    for ch in s1:
        if not seen[ord(ch)]:
            result.append(ch)

    return ''.join(result)

if __name__ == "__main__":

    s1 = "hello world"
    s2 = "lo"
    print(rem(s1,s2))