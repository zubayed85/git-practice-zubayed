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
    if b != 0:
        return a / b
    else:
        return "Undefined (division by zero)"
