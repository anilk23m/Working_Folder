#modules and packages -
#A module is simply a .py file that contains python code (functions, classes, variables) that you can re use in other files
#Think of it like a resource file - you will write the utilities and import them wherever needed.

def login_info(message):
    print(f"[INFO] - {message}")

def log_error(message):
    print(f"[ERROR] - {message}")

max_retries = 3

#package is the combination of multiple .py module files
#module - a single .py file
#package - a folder containing multiple .py file
