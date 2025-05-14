# Positional parameters
def greet_user(name, age):
    print(f"Hello, my name is {name} and I'm turning {age} this year")

greet_user("Yocki", 24)

# Default parameter
def favorite_food(name, food="Beef Suya"):
    print(f"{name}'s favorite food is {food}")

favorite_food("Adrian")

# Keyword parameter
def class_marks(name, marks):
    print(f"{name} has scored {marks} in the test")

class_marks(marks=90, name="Johanna")
