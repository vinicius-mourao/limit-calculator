# import sympy to use the function in an appropriate way
from sympy import *

# define x as the variable
x = symbols('x')

def get_function():
  """Function that is responsible for recieving the user's function"""
  function = input("Type your function, f(x) (ex: 2*x**3 + 3*x + 3 ): ")
  f = sympify(function)
  return f

def calculate_limit(f):
  """Function that is responsible for calculating the limit by substituting the x with the value it approaches (user's input)."""
  point = int(input("What value does x approach in the limit? "))
  limit = f.subs(x, point)

  # if an indeterminate form appears, the program calculates using other mathematical methods until it is solved
  if limit is S.NaN or limit is S.ComplexInfinity:
    print('Indeterminate form, trying another approach by factoring.')
    f_factored = factor(f)
    limite = f_factored.subs(x, point)
    if limit is S.NaN or limit is S.ComplexInfinity:
      print("Factoring inefficient. Trying L'Hopital.")
      num, den = fraction(f)
      limit = diff(num, x).subs(x, point) / diff(den, x).subs(x, point)
  return limit


f = get_function()
print(calculate_limit(f))