def non_repeating(s):
    freq = [0] * 256  

    
    for ch in s:
        if ch != ' ':
            freq[ord(ch)] += 1

    
    for ch in s:
        if freq[ord(ch)] == 1:
            print(ch, end="")


if __name__ == "__main__":
    s = "hello world"
    non_repeating(s)