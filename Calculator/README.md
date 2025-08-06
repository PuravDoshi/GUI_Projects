# 🧮 Simple GUI Calculator (Tkinter)

This is a basic calculator app built using **Python's Tkinter library**. It allows users to perform simple arithmetic operations: **addition, subtraction, multiplication, and division** through a graphical interface.

---

## 🚀 Features

- Clean and intuitive **GUI** layout
- Supports:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x`)
  - Division (`/`)
- Error handling for division by zero
- Clear (`C`) button to reset input
- Buttons styled with color for a better user experience
- Responsive label showing ongoing input and results

---

## 🛠️ Tech Used

- **Python 3.x**
- **Tkinter** (Python's standard GUI library)

---

## 📁 File Structure
``` bash
Calculator/
├── app.py # Main application code
├── README.md # Project documentation
```
## 🧠 How It Works
- Digits are appended to the display using the get_digit() function.
- On pressing an operator (+, -, etc.), the current value is stored as the first number.
- After entering the second number and pressing =, the result is calculated.
- All text displayed is updated using the Label['text'] property (since Labels do not support .get() like Entry widgets).

## 📌 Notes
- lambda: is used to pass arguments to button functions without immediately calling them.
- highlightbackground is used for button coloring on macOS systems.
- Label['text'] is used instead of .get() to retrieve display values, as Label is not an input widget.