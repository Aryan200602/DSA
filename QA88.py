#Print max length word in a string

def maxi(s):

    words = s.split()
    max_len = 0
    max_word = ""

    for word in words:
        max_len = max(max_len, len(word))
        if (len(word) == max_len):
            max_word = word

    print(max_word)

if __name__ == "__main__":
    s = "My name is Aryan"
    maxi(s)
