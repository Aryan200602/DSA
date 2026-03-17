# Function to calculate GCD using Euclid's Algorithm
def gcd(a, b):
    if b == 0:
        return a  
    return gcd(b, a % b)  # Recursively call GCD with (b, a % b)

# Function to calculate LCM using the GCD
def calculateLCM(a, b):
    g = gcd(a, b)  
    return (a * b) // g  # Calculate LCM using the formula LCM = (a * b) / GCD


a, b = 4, 8
lcm = calculateLCM(a, b)  
print(f"The LCM of the two given numbers is {lcm}")  