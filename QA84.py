#find the non repeating words in the string 

def nrep(s):

    freq={}
    words=s.split()

    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    for word in words:
        if freq[word]==1:
            print(word,end=" ")

if __name__ == "__main__":

    s = "hello hello world world welcome to DSA"
    nrep(s)