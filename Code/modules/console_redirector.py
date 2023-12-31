# console_redirector.py
import sys
import tkinter as tk

class ConsoleRedirector:
    def __init__(self, console_widget):
        self.console_widget = console_widget

    def write(self, text):
        self.console_widget.insert(tk.END, text)
        self.console_widget.see(tk.END)
