# import sympy to use the function in an appropriate way
from sympy import *
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# define streamlit webpage title
st.set_page_config(page_title="Limit Calculator and Visualizer", layout="wide")
st.title("Limit Calculator and Visualizer", width= 'stretch', text_alignment='center')
st.subheader("_*:red[Calculate]* the limit requested and *:blue[visualize]* the function for better understanding_", text_alignment='center')


# define x as the variable
x = symbols('x')

def get_function():
  """Function that is responsible for recieving the user's function"""
  function = st.text_input("Type your function (ex: 2*x**3 + 3*x + 3 )", icon = "📊")
  if not function:
    return None
  try:
    f = sympify(function)
    return f
  except Exception:
    return None
    
def calculate_limit(f):
  """Function that is responsible for calculating the limit by substituting the x with the value it approaches (user's input)."""
  point = st.text_input("What value does x approach in the limit? (type 'oo' for infinity): ", icon = "➡️")
  if not point:
    return None
  try:
    point = sympify(point)
  except Exception:
    return None
  
  result = limit(f, x, point)
  return result, point

def show_limit(result):
  if result is None:
    result = ""
  st.subheader(f"Result: {result}")
  st.divider()

def plot_function(f, point):
  st.subheader("Function graph showing the limit")
  
  # Convert to float
  try:
    point_float = float(point)
  except:
    st.warning("Could not plot for infinite limits.")
    return
  
  # create x margin
  margin = 5
  x_vals = np.linspace(point_float -margin, point_float + margin, 500)

  # convert sympy function to numerical
  f_numeric = lambdify(x, f, 'numpy')

  # Calculate y values, masking invalid ones
  with np.errstate  (divide = 'ignore', invalid = 'ignore'):
    y_vals = f_numeric(x_vals)
    y_vals = np.where(np.isfinite(y_vals,), y_vals, np.nan)

  # Plot
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode = 'lines', name = str(f)))
  fig.add_vline(x=point_float, line_dash='dash', line_color='red', annotation_text=f'x → {point_float}')
  fig.update_layout(xaxis_title='x', yaxis_title='f(x)')
    
  st.plotly_chart(fig, use_container_width=True)



f = get_function()
if f is not None:
    calc = calculate_limit(f)
    if calc is not None:
      result, point = calculate_limit(f)
      show_limit(result)
      plot_function(f, point)