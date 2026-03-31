# Limit Calculator and Visualizer

An interactive tool that calculates mathematical limits symbolically 
using SymPy and visualizes the function graph around the limit point 
with Plotly, built with Python and Streamlit.

## Features

- Symbolic limit calculation using SymPy
- Supports indeterminate forms (0/0, ∞/∞, 0·∞, 1^∞)
- Interactive function graph with Plotly
- Visual marker at the limit point
- Supports infinity as input (`oo`)
- Graceful error handling for unsolvable limits

## Supported Syntax

| Math notation | Input |
|---|---|
| x² | x**2 |
| eˣ | exp(x) |
| ln(x) | log(x) |
| sin(x) | sin(x) |
| √x | sqrt(x) |
| ∞ | oo |

## Technologies

- Python
- Streamlit
- SymPy
- Plotly
- NumPy

## How to Run
```bash
pip install streamlit sympy plotly numpy
streamlit run limit_calculator.py
```

## Examples

| Function | Point | Result |
|---|---|---|
| x**2 | 0 | 0 |
| sin(x)/x | 0 | 1 |
| (1 - cos(x))/x**2 | 0 | 1/2 |
| exp(x)/x | oo | ∞ |
| x*log(x) | 0 | 0 |

## Known Limitations

- Cannot plot limits at infinity
- Some complex expressions may raise `NotImplementedError` from SymPy

## Author

Vinícius Mourão Mendes Costa  