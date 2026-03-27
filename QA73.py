#print the ascii value of a character

def ascii_value(char):
    return ord(char)

if __name__ == "__main__":
    character = input("Enter a character: ")
    print(f"The ASCII value of '{character}' is: {ascii_value(character)}")