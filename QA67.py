#Convert digits/ numbers to words: 

def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen",
             "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]

    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        return tens[n//10] + " " + ones[n%10]
    elif n < 1000:
        return ones[n//100] + " hundred " + number_to_words(n%100)

# Example
print(number_to_words(507))