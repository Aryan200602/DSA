#print the number of vowels, consonants and spaces are present in the given string:

def count(s):

    vc=0
    sp=0
    cc=0

    n=len(s)
    s=s.lower()
    for i in range(n):
        if s[i] in "aeiou":
            vc+=1
        elif s[i]==" ":
            sp+=1
        else: 
            cc+=1
    
    print("Vowels:",vc)
    print("Consonants:",cc)
    print("Spaces:",sp)

if __name__ == "__main__":
    s="hello world"
    count(s)
