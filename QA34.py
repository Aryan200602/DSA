# greatest of two numbers

def greatest_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

if __name__ == "__main__":
    number1 = 25
    number2 = 30
    result = greatest_of_two_numbers(number1, number2)
    print(f"The greatest of the two numbers is: {result}")