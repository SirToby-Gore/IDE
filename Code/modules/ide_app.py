import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from modules import *

class IDEApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IDE")

        # Initial theme settings
        self.ui_color = "white"

        # Create text and console widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file_dialog)
        file_menu.add_command(label="Save", command=self.save_file_dialog)
        file_menu.add_command(label="Save As", command=self.save_as_file_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.destroy)

        # Create Options menu
        options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        options_menu.add_command(label="Toggle Light Mode", command=self.toggle_light_mode)
        options_menu.add_separator()
        colors = ["Red", "Green", "Blue", "Black", "White"]
        for color in colors:
            options_menu.add_command(label=f"Set UI Color to {color}", command=lambda c=color.lower(): self.set_ui_color(c))

        # Create Features menu
        features_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Features", menu=features_menu)
        features_menu.add_command(label="Run Features Tab", command=self.run_features_tab)
        features_menu.add_command(label="GitHub Integration", command=self.run_github_integration)
        features_menu.add_command(label="Run Search Engine", command=self.run_search_engine)

        # Text widget for code input
        self.text_widget = tk.Text(self.master, wrap=tk.WORD, width=80, height=20, bg=self.ui_color, fg="black")
        self.text_widget.pack(padx=10, pady=10)

        # Console widget for output
        self.console_widget = tk.Text(self.master, wrap=tk.WORD, width=80, height=10, bg=self.ui_color, fg="black")
        self.console_widget.pack(padx=10, pady=10)

        # Run button
        self.run_button = tk.Button(self.master, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)

    def open_file_dialog(self):
        file_name = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_name:
            content = open_file(file_name)
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, content)

    def save_file_dialog(self):
        file_name = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_name:
            # Retrieve content from the text widget
            content = self.text_widget.get(1.0, tk.END)
            message = save_file(file_name, content)
            self.status_bar.config(text=message)

    def save_as_file_dialog(self):
        file_name = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_name:
            # Retrieve content from the text widget
            content = self.text_widget.get(1.0, tk.END)
            message = save_as_file(file_name, content)
            self.status_bar.config(text=message)

    def run_code(self):
        # Get code from the text widget
        code = self.text_widget.get(1.0, tk.END)

        try:
            # Execute the code
            exec(code)
            self.console_widget.insert(tk.END, "Code executed successfully.\n")
        except Exception as e:
            # Handle exceptions
            self.console_widget.insert(tk.END, f"Error: {e}\n")

    def toggle_dark_mode(self):
        # Toggle between dark and light mode
        self.master.option_add("*TButton*highlightBackground", self.ui_color)
        self.master.option_add("*TButton*highlightColor", self.ui_color)
        self.master.option_add("*TButton*foreground", "white")
        self.master.option_add("*TButton*background", "black")
        ttk.Style().theme_use("default")

    def toggle_light_mode(self):
        # Toggle between dark and light mode
        self.master.option_add("*TButton*highlightBackground", self.ui_color)
        self.master.option_add("*TButton*highlightColor", self.ui_color)
        self.master.option_add("*TButton*foreground", "black")
        self.master.option_add("*TButton*background", "white")
        ttk.Style().theme_use("clam")

    def set_ui_color(self, color):
        # Set the UI color
        color_dict = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF", "black": "#000000", "white": "#FFFFFF"}
        self.ui_color = color_dict[color]
        self.text_widget.config(bg=self.ui_color)
        self.console_widget.config(bg=self.ui_color)
        self.master.option_add("*TButton*highlightBackground", self.ui_color)
        self.master.option_add("*TButton*highlightColor", self.ui_color)

    def run_features_tab(self):
        # Placeholder for running features tab logic
        self.console_widget.insert(tk.END, "Running Features Tab...\n")

    def run_github_integration(self):
        # Placeholder for running GitHub integration logic
        self.console_widget.insert(tk.END, "Running GitHub Integration...\n")

    def run_search_engine(self):
        # Placeholder for running search engine logic
        self.console_widget.insert(tk.END, "Running Search Engine...\n")

# Add this if __name__ block at the end of the file
if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)
    root.mainloop()
