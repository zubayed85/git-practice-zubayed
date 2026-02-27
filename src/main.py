print("Md.Zubayed Hossain")

from datetime import date

today = date.today()
print(today)

# Import the specific function from the utils module
from utils import add


# Import the specific function from the utils module
from utils import subtract

# Import the specific function from the utils module
from utils import multiply

# Import the specific function from the utils module
from utils import divition

# Define variables to use for the addition and subtraction
num1 = 25
num2 = 10

# Call the add function with your variables
result_of_add = add(num1, num2)

# Call the subtract function with your variables
result_of_subtract = subtract(num1, num2)

# Print the result
print(f"The Summation of {num1} and {num2} is: {result_of_add}")

# Print the result
print(f"The difference between {num1} and {num2} is: {result_of_subtract}")
