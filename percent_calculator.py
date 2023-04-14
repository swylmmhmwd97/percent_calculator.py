# percent_calculator.py

def percent_calculator(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Example usage
print(percent_calculator(10000, 5, 2)) # Output: 1000.0
