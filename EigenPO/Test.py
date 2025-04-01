import tkinter as tk

def open_main_window():
    """ Closes the Welcome Window and opens the Main Application Window """
    welcome_window.withdraw()  # Hide the Welcome Window
    main_window.deiconify()  # Show the Main Application Window

def go_back_to_welcome():
    """ Closes the Main Window and reopens the Welcome Window """
    main_window.withdraw()  # Hide the Main Window
    welcome_window.deiconify()  # Show the Welcome Window

# Step 1: Create the Welcome Window
welcome_window = tk.Tk()
welcome_window.title("Welcome Window")
welcome_window.geometry("500x300")

tk.Label(welcome_window, text="Welcome to My Program!", font=("Arial", 16)).pack(pady=20)
tk.Button(welcome_window, text="Continue", command=open_main_window).pack(pady=10)

# Step 2: Create the Main Application Window (Initially Hidden)
main_window = tk.Toplevel()
main_window.withdraw()  # Keep it hidden initially
main_window.title("Main Application")
main_window.geometry("600x400")

tk.Label(main_window, text="This is the Main Window", font=("Arial", 16)).pack(pady=20)
tk.Button(main_window, text="Go Back to Welcome", command=go_back_to_welcome).pack(pady=10)

# Start the Tkinter event loop
welcome_window.mainloop()