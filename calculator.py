from typing import Union
import streamlit as st  # type: ignore

# Title of the web app
st.title("Simple Calculator")

# Input fields for the two numbers
number1 = st.number_input("Enter first number", format="%f")
number2 = st.number_input("Enter second number", format="%f")

# Radio buttons for selecting the operation
operation = st.radio("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Initialize result
result: Union[int, float, None] = None

# Calculate the result based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = number1 + number2
    elif operation == "Subtract":
        result = number1 - number2
    elif operation == "Multiply":
        result = number1 * number2
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
        else:
            st.error("Cannot divide by zero")
            result = None
    
    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")
