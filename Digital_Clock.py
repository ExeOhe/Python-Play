import datetime
import tkinter as tk

def update_time():
    current_time = datetime.datetime.now().strftime("The time is currently : %I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update the time every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and pack the label to display the time
time_label = tk.Label(root, font=('Helvetica', 48), fg='white')
time_label.pack()

# Call the update_time function to initialize the display
update_time()

# Start the Tkinter event loop
root.mainloop()