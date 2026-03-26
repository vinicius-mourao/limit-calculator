# 📘 Limit Calculator (Experimental) – SymPy

This project is an experimental limit calculator built in Python using SymPy.
Instead of relying on the built-in `limit()` function, it attempts to compute limits manually by applying mathematical techniques such as substitution, factoring, and L'Hôpital's Rule.

## 🚀 Features

* Accepts user-defined functions
* Substitutes values directly to evaluate limits
* Detects indeterminate forms (e.g. `0/0`, `∞/∞`)
* Attempts alternative methods:

  * Factoring
  * L'Hôpital's Rule (via derivatives)

## 🛠️ Technologies

* Python
* SymPy (symbolic mathematics library)

## ▶️ How to Run

1. Install SymPy (if not installed):

   ```bash
   pip install sympy
   ```

2. Run the program:

   ```bash
   python main.py
   ```

3. Input a function and the value that `x` approaches:

   ```
   Type your function: x*log(x)
   What value does x approach in the limit? 0
   ```

## ⚠️ Limitations

* Does not use SymPy's `limit()` function (by design)
* Only partially handles indeterminate forms
* L'Hôpital's Rule is applied in a simplified way
* Some limits (e.g. products like `0 * ∞`) may not be handled correctly yet
* No support for one-sided limits (`x → 0⁺` or `x → 0⁻`)

## 💡 Future Improvements

* Detect and handle more indeterminate forms:

  * `0 · ∞`
  * `1^∞`, `0^0`, `∞^0`
* Automatically rewrite expressions before applying L'Hôpital
* Improve validation and error handling
* Support directional limits
* Build a cleaner CLI interface

## 📌 Purpose

This project was created for learning purposes, to better understand:

* How limits work mathematically
* How symbolic computation can be implemented
* The logic behind L'Hôpital's Rule

## 👨‍💻 Author

Developed by Vinícius Mourão Mendes Costa

---
