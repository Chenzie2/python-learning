# 01. Defining functions using the def keyword
def greet():
    """Prints a simple greeting."""
    print("Hello, world!")


# 02. Function parameters (positional, keyword, default values)
def describe_person(name, age=30, city="Unknown"):
    """Describes a person with name, age, and city."""
    print(f"{name} is {age} years old and lives in {city}.")


# 03. *args for variable number of positional arguments
def add_numbers(*args):
    """Returns the sum of any number of numeric arguments."""
    return sum(args)


# 04. **kwargs for variable number of keyword arguments
def print_info(**kwargs):
    """Prints key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 05. return statement for outputting values
def square(num):
    """Returns the square of a number."""
    return num ** 2


# 06. Docstrings for documenting functions
def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The result of a * b.
    """
    return a * b


# 07. Scope of variables (local vs global)
x = 10  # Global variable

def change_x():
    x = 5  # Local variable
    print("Inside function, x =", x)

# Uncomment to use global:
# def change_x_global():
#     global x
#     x = 5


# 08. Lambda functions (anonymous functions)
square_lambda = lambda x: x ** 2


# 09. Higher-order functions (functions operating on other functions)
def apply_function(func, value):
    """Applies a function to a value."""
    return func(value)


# Testing the functions
if __name__ == "__main__":
    greet()
    describe_person("Alice")
    describe_person("Bob", 25, "Paris")

    print("Sum:", add_numbers(1, 2, 3, 4, 5))

    print_info(name="Charlie", age=40, job="Engineer")

    print("Square:", square(6))

    print("Multiply:", multiply(3, 4))

    print("Global x =", x)
    change_x()
    print("After function call, global x =", x)

    print("Lambda square of 7:", square_lambda(7))

    print("Apply square using higher-order function:", apply_function(square, 8))
