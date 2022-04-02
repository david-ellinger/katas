import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
USER_INP = simpledialog.askstring(title="Input Test", prompt="Type your name")

print("Hello", USER_INP)
