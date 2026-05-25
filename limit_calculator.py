from sympy import symbols, sympify, limit, diff, integrate, oo, lambdify
import streamlit as st
import plotly.graph_objects as go
import numpy as np

x = symbols('x')

st.set_page_config(page_title="Calculadora de Limites", layout="wide")
st.title("Calculadora de limites e visualizador")
st.subheader("_*:red[Calcule]* limites, derivadas e integrais — e *:blue[visualize]* a função_")

# ── Inputs ────────────────────────────────────────────────────────────────────

col_f, col_p = st.columns(2)

with col_f:
    raw_function = st.text_input("Função f(x)", placeholder="ex: sin(x)/x", key="input_function")

with col_p:
    raw_point = st.text_input("Valor ao qual x tende", placeholder="ex: 0  ou  oo", key="input_point")

# ── Processamento ─────────────────────────────────────────────────────────────

if not raw_function or not raw_point:
    st.info("Digite a função e o valor de x para começar.")
    st.stop()

try:
    f = sympify(raw_function)
except Exception:
    st.error("Função inválida. Verifique a sintaxe (use * para multiplicação, ** para expoentes).")
    st.stop()

try:
    point = sympify(raw_point)
except Exception:
    st.error("Valor de x inválido. Use um número ou 'oo' para infinito.")
    st.stop()

# ── Cálculos ──────────────────────────────────────────────────────────────────

limit_result = limit(f, x, point)
derivative   = diff(f, x)
integral     = integrate(f, x)

# ── Resultados ────────────────────────────────────────────────────────────────

st.divider()
col1, col2, col3 = st.columns(3)

col1.metric(label="Limite",      value=str(limit_result))
col2.metric(label="Derivada", value=str(derivative))
col3.metric(label="Integral",   value=str(integral) + " + C")

# ── Plot ──────────────────────────────────────────────────────────────────────

st.divider()
st.subheader("Gráfico da função")

try:
    point_float = float(point)
    margin      = 5
    x_vals      = np.linspace(point_float - margin, point_float + margin, 600)

    f_numeric = lambdify(x, f, 'numpy')

    with np.errstate(divide='ignore', invalid='ignore'):
        y_vals = f_numeric(x_vals)
        y_vals = np.where(np.isfinite(y_vals), y_vals, np.nan)

    # Reta tangente: y = f(a) + f'(a) * (x - a)
    fa        = float(f.subs(x, point))
    dfa       = float(derivative.subs(x, point))
    y_tangent = fa + dfa * (x_vals - point_float)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines',
                             name=f"f(x) = {raw_function}"))

    fig.add_trace(go.Scatter(x=x_vals, y=y_tangent, mode='lines',
                             name=f"Tangent em x={point_float}  [slope={dfa:.3f}]",
                             line=dict(color='orange', dash='dot')))

    fig.add_trace(go.Scatter(x=[point_float], y=[fa], mode='markers',
                             name=f"f({point_float}) = {fa:.3f}",
                             marker=dict(color='red', size=10)))

    fig.add_vline(x=point_float, line_dash='dash', line_color='red',
                  annotation_text=f"x → {point_float}")

    fig.update_layout(xaxis_title='x', yaxis_title='f(x)', height=450)
    st.plotly_chart(fig, use_container_width=True)

except (TypeError, ValueError, AttributeError):
    st.info("Gráfico não disponível para limites complexos ou infinitos.")