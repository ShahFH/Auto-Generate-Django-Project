import os
import subprocess

def generate_django_project(project_name):
    # Create the project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create and activate a virtual environment
    subprocess.run(["python", "-m", "venv", "venv"])
    if os.name == "nt":
        subprocess.run(["venv\\Scripts\\activate.bat"], shell=True)
    else:
        subprocess.run(["source", "venv/bin/activate"], shell=True)

    # Upgrade pip
    subprocess.run(["pip", "install", "--upgrade", "pip"])

    # Install Django and other necessary libraries
    subprocess.run(["pip", "install", "django", "django-widget-tweaks"])

    # Create the Django project
    subprocess.run(["django-admin", "startproject", project_name, "."])

    # Deactivate the virtual environment
    subprocess.run(["deactivate"], shell=True)

    print(f"Successfully generated Django project: {project_name}")

# Usage
project_name = input("Enter the name of your Django project: ")
generate_django_project(project_name)

# Instructions for activating the virtual environment
if os.name == "nt":
    print("Activate the virtual environment using: venv\\Scripts\\activate.bat")
else:
    print("Activate the virtual environment using: source venv/bin/activate")
