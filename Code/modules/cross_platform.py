# cross_platform.py

import platform
import subprocess

def run_on_vm(vm_name, iso_path):
    # Detect the operating system
    os_system = platform.system()

    # Run the appropriate command based on the operating system
    if os_system == "Windows":
        start_vm_windows(vm_name)
    elif os_system == "Linux":
        start_vm_linux(vm_name, iso_path)
    elif os_system == "Darwin":  # macOS
        start_vm_macos(vm_name)
    elif os_system == "Android":  # Just an example, you may need a different approach for Android
        start_vm_android(vm_name)
    else:
        print("Unsupported operating system.")

def start_vm_windows(vm_name):
    # Placeholder for starting a VM on Windows
    try:
        # Example command to start a VM on Windows using VBoxManage
        command = f"VBoxManage startvm {vm_name} --type headless"

        # Run the command using subprocess
        subprocess.run(command, shell=True, check=True)

        print(f"VM '{vm_name}' started successfully on Windows.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting VM on Windows: {e}")

def start_vm_linux(vm_name, iso_path):
    # Placeholder for starting a VM on Linux
    try:
        # Example command to start a VM on Linux using QEMU
        command = f"qemu-system-x86_64 -name {vm_name} -boot d -cdrom {iso_path}"

        # Run the command using subprocess
        subprocess.run(command, shell=True, check=True)

        print(f"VM '{vm_name}' started successfully on Linux.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting VM on Linux: {e}")

def start_vm_macos(vm_name):
    # Placeholder for starting a VM on macOS
    try:
        # Example command to start a VM on macOS using a different tool
        command = f"your_custom_command_here {vm_name}"

        # Run the command using subprocess
        subprocess.run(command, shell=True, check=True)

        print(f"VM '{vm_name}' started successfully on macOS.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting VM on macOS: {e}")

def start_vm_android(vm_name):
    # Placeholder for starting a VM on Android
    print(f"Starting VM '{vm_name}' on Android is not supported in this example.")
    # You would need a different approach for running VMs on Android, possibly using Android emulators.

# Example usage:
# run_on_vm("YourVMName", "path/to/your/iso/file.iso")
