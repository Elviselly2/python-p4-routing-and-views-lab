#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print String Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Log the text in the console
    return f"{text}"  # Display in browser

# Count Route
@app.route('/count/<int:num>')
def count(num):
    return "\n".join(str(i) for i in range(num))+"\n"  # Numbers on separate lines

# Math Operation Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "div": num1 / num2 if num2 != 0 else "Cannot divide by zero",
        "%": num1 % num2
    }
    return str(operations.get(operation, "Invalid operation"))  # Returns only the number


if __name__ == '__main__':
    app.run(debug=True, port=5555)

