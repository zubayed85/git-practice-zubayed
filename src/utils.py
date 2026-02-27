def add(a, b):
  """
  Adds two numbers, a and b, and returns the result.
  """
  result = a + b
  return result


def subtract(a, b):
  """Subtracts b from a and returns the result."""
  return a - b

def multiply(a, b):
  """
  Multiplies two numbers, a and b, and returns the product.
  """
  result = a * b
  return result


def divition(a, b):
    """
    Performs true division of a by b and returns the result as a float.
    Handles division by zero.
    """
    try:
        # Code that might raise an exception is placed in the try block
        result = a / b
    except ZeroDivisionError:
        # Code to handle the specific error (division by zero)
        return "Error: Cannot divide by zero."
    else:
        # Code that runs only if no exception occurred in the try block
        return result
    finally:
        # Code that always runs, regardless of whether an error occurred or not
        print("Division attempt finished.")