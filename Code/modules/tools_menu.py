# tools_menu.py
import tkinter as tk

class ToolsMenu:
    @staticmethod
    def create_tools_menu(master, ui_color, console_widget, text_widget):
        tools_menu = tk.Menu(master, tearoff=0)
        master.menu_bar.add_cascade(label="Tools", menu=tools_menu)

        # Each element in the "Tools" menu is now a separate list
        tools_menu.add_command(label="Run Features Tab", command=lambda: ToolsMenu.run_features_tab(console_widget))
        tools_menu.add_command(label="GitHub Integration", command=lambda: ToolsMenu.run_github_integration(console_widget))
        tools_menu.add_command(label="Run Search Engine", command=lambda: ToolsMenu.run_search_engine(console_widget))

    @staticmethod
    def run_features_tab(console_widget):
        # Placeholder for running features tab logic
        console_widget.insert(tk.END, "Running Features Tab...\n")

    @staticmethod
    def run_github_integration(console_widget):
        # Placeholder for running GitHub integration logic
        console_widget.insert(tk.END, "Running GitHub Integration...\n")

    @staticmethod
    def run_search_engine(console_widget):
        # Placeholder for running search engine logic
        console_widget.insert(tk.END, "Running Search Engine...\n")
