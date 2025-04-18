import datetime
import tkinter as tk
import os

def update_time():
    current_time = datetime.datetime.now().strftime("The time is currently : %I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update the time every second

def check_repo():
    if os.path.isdir(".git"):
        print("This directory is a git repository.")
    else:
        print("This directory is not a git repository.")

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and pack the label to display the time
time_label = tk.Label(root, font=('Helvetica', 48), fg='white')
time_label.pack()

# Call the update_time function to initialize the display
update_time()

# Check if there is a repository for this file
check_repo()

# Start the Tkinter event loop
root.mainloop()