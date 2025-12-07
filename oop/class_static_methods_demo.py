

class Calculator:
    """
    A class containing examples of static and class methods to illustrate 
    their differences and usage.
    """
   
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Takes two arguments and returns their sum.
        It does not need access to the class (cls) or instance (self) state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Takes the class itself (cls) as the first argument.
        It uses 'cls' to access the class attribute 'calculation_type'.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

