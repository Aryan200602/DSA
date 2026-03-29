#print frequecy of characters in a string

def char_frequency(s):
    freq=[0]*26

    for c in s:
        if c.isalpha():
            index=ord(c.lower())-ord('a')
            freq[index]+=1

    for i in range(26):
        if freq[i]>0:
            print(f"{chr(i+ord('a'))}: {freq[i]}")
            
if __name__ == "__main__":
    s = "hello world"
    char_frequency(s)
