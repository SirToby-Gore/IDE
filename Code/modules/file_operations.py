# file_operations.py
import os

def open_file(file_name):
    try:
        file_path = os.path.join("C:\\Users\\User\\Documents\\My IDE\\Code\\Files", file_name)
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"

def save_file(file_name, content):
    try:
        file_path = os.path.join("C:\\Users\\User\\Documents\\My IDE\\Code\\Files", file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        return "File saved successfully."
    except Exception as e:
        return f"Error saving file: {e}"

def save_as_file(file_name, content):
    try:
        file_path = os.path.join("C:\\Users\\User\\Documents\\My IDE\\Code\\Files", file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        return "File saved successfully."
    except Exception as e:
        return f"Error saving file: {e}"

def new_file():
    return "New file created."

def print_file(file_name):
    try:
        file_path = os.path.join("C:\\Users\\User\\Documents\\My IDE\\Code\\Files", file_name)
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"
