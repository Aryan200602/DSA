#count the number of words in the sentence.

def count(s):
    count = 1
    for ch in s:
        if ch == ' ':
            count += 1

    return count 

if __name__ == "__main__":
    s = "My name is Aryan"
    print(count(s))
    