# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Driver code
year = 2024  # Year to check

# Check if the year is a leap year using the function
if is_leap_year(year):
    print("Yes")  # Output "Yes" if it's a leap year
else:
    print("No")  # Output "No" if it's not a leap year