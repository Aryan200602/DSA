#make all the first element and last element of the words capital

def capital(s):
    s=list(s)
    n=len(s)
    s[0]=s[0].upper()
    s[n-1]=s[n-1].upper()


    for i in range(n):
        if s[i] == ' ':
            s[i-1]=s[i-1].upper()
            if i+1<n:
                s[i+1]=s[i+1].upper()
    return ''.join(s)

if __name__ == "__main__":
    sentence = "my name is aryan"
    sentence=capital(sentence)
    print(sentence)
            


