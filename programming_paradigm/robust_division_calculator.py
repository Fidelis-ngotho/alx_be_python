# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Non-numeric input provided. Please enter numeric values only."
    
    return f"The result of dividing {num} by {denom} is {result}."