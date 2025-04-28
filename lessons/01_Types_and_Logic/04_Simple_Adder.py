"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
num1 = simpledialog.askinteger("number 1", "Enter the first number to be added")
# Ask the user for the second number
num2 = simpledialog.askinteger("number 2", "Enter the second number to be added")
# Display the sum of the two numbers 
num3 = num1 + num2
messagebox.showinfo(' ', "the sum of those two numbers is " + str(num3))
# Keep the window open
# no :)

