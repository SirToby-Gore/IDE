import tkinter as tk
from modules import  *

if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)

    # Create File menu
    app.menu_bar.add_cascade(label="File", menu=app.file_menu)
    app.file_menu.add_command(label="Open", command=app.open_file_dialog)
    app.file_menu.add_command(label="Save", command=app.save_file_dialog)
    app.file_menu.add_command(label="Save As", command=app.save_as_file_dialog)
    app.file_menu.add_separator()
    app.file_menu.add_command(label="Exit", command=root.destroy)

    # Create additional menus as needed
    app.create_menu("Add Log Points", app.add_log_points)
    app.create_menu("Word Suggestions", app.word_suggestions)
    app.create_menu("Python Standardization Checks", app.python_standardization_checks)
    app.create_menu("Auto Bracketing", app.auto_bracketing)
    app.create_menu("Set Visual Modes", app.set_visual_modes)
    app.create_menu("Local File Operations", app.run_local_file_operations)
    app.create_menu("GitHub Operations", app.run_github_operations)

    # Add the Features Tab, GitHub Integration, and Search Engine menu items
    ToolsMenu.create_tools_menu(app, app.ui_color, app.console_widget, app.text_widget)

    root.mainloop()
