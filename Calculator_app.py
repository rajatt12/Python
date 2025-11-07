import streamlit as st

st.title("Simple Calculator App")

# Input numbers
a = st.number_input("Enter first number (a):", value=0.0, format="%.6f")
b = st.number_input("Enter second number (b):", value=0.0, format="%.6f")

# Select operation
operation = st.selectbox(
    "Choose the operation you want to perform:",
    [
        "+  (a + b)",
        "-  (a - b)",
        "*  (a * b)",
        "/  (a / b)",
        "%  (a % b)",
        "** (a ^ b)",
        ">= (a >= b)",
        "<= (a <= b)",
        "== (a == b)",
        "!= (a != b)"
    ]
)

# Compute result
result = None
error = None

try:
    if operation.startswith("+"):
        result = a + b
    elif operation.startswith("-"):
        result = a - b
    elif operation.startswith("*"):
        result = a * b
    elif operation.startswith("/"):
        if b == 0:
            error = "Division by zero is not allowed."
        else:
            result = a / b
    elif operation.startswith("%"):
        if b == 0:
            error = "Modulo by zero is not allowed."
        else:
            result = a % b
    elif operation.startswith("**"):
        result = a ** b
    elif operation.startswith(">="):
        result = a >= b
    elif operation.startswith("<="):
        result = a <= b
    elif operation.startswith("=="):
        result = a == b
    elif operation.startswith("!="):
        result = a != b
except Exception as e:
    error = f"Error computing result: {e}"

# Display result or error
if error:
    st.error(error)
else:
    st.success(f"Result: {result}")
