# Greatest of three numbers

def greatest_of_three_numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
    number1 = 25
    number2 = 30
    number3 = 20
    result = greatest_of_three_numbers(number1, number2, number3)
    print(f"The greatest of the three numbers is: {result}")