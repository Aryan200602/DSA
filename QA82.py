# Check if two strings are anagrams of each other

def anagrams(s1,s2):
    freq=[0]*256

    if len(s1)!=len(s2):
        return False

    for ch in s1:
        freq[ord(ch)]+=1

    for ch in s2:
        freq[ord(ch)]-=1

    for i in range(256):
        if freq[i]!=0:
            return False

    return True 

if __name__ == "__main__":

    s1 = "listen"
    s2 = "silent"
    if anagrams(s1, s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

