#find the max frequency character in a string

def maxfreq(s):
    freq=[0]*256
    max=0

    for ch in s:
        if ch!=' ':
            freq[ord(ch)]+=1
        
    for ch in s:
        if freq[ord(ch)]>max:
            max=freq[ord(ch)]
            maxch=ch

    print(f"Maximum frequency character: {maxch} with frequency {max}")

if __name__ == "__main__":
    s = "hello world"
    maxfreq(s)