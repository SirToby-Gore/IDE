# version_control.py
import os

def git_branching(repository_path, branch_name):
    if not os.path.exists(repository_path):
        print(f"Error: Repository path '{repository_path}' does not exist.")
        return

    try:
        os.chdir(repository_path)
        # Rest of the git_branching logic here
    except Exception as e:
        print(f"Error: {e}")
