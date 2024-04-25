import tkinter as tk
from tkinter import messagebox


def welcomeMessage(username):
    #Create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is Python GUI with Tkinter")
    label_2.pack()

    #Run the Tkinter event loop
    window.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        messagebox.showerror("Login", "Invalid username or password")
        # Create the main Tkinter window
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the Tkinter event loop
root.mainloop()

