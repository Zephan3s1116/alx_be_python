#!/usr/bin/env python3
"""
Contains the safe_divide function that performs division while robustly 
handling ZeroDivisionError and ValueError (non-numeric input).
"""

def safe_divide(numerator, denominator):
    """
    Divides two inputs, handling division by zero and non-numeric inputs.

    Args:
        numerator (str or numeric): The dividend.
        denominator (str or numeric): The divisor.

    Returns:
        str or float: The result of the division as a float, or an error message string.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle the case where conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."

# End of robust_division_calculator.py