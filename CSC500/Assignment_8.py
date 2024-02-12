# Class definition
class House:
    def __init__(self, color, area):
        self.color = color
        self.area = area
        self.__price = 100000  # Private attribute

# Instance creation
my_house = House("Blue", 2000)

# Accessing public attributes
print(my_house.color)  # Output: Blue
print(my_house.area)   # Output: 2000

# Attempting to access private attribute directly
# This would raise an AttributeError
print(my_house.__price)