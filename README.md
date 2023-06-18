
# Django Project auto Generator

This is a Python script that automates the process of generating a Django project. It creates a new Django project directory, sets up a virtual environment, installs Django and necessary libraries, and generates the Django project structure.

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Usage

1. Clone or download the script file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

\```bash
python script_name.py
\```

Replace `script_name.py` with the actual name of the script file.

4. Enter the desired name for your Django project when prompted.

5. Wait for the script to complete the project generation process.

6. After the script finishes, you will see instructions for activating the virtual environment based on your operating system:

- On Windows: `venv\Scripts\activate.bat`
- On macOS/Linux: `source venv/bin/activate`

Make sure to activate the virtual environment before running any Django commands in the project directory.

7. Start working on your Django project!

## Notes

- The script uses the `venv` module to create and manage the virtual environment.
- It upgrades pip to the latest version before installing Django and other necessary libraries.
- The script assumes you have Django and `django-widget-tweaks` as the required libraries. Modify the script if you need additional libraries.
- The generated Django project will be located in a directory with the name you provided.
