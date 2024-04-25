import tkinter as tk

# Handling button click event
def button_click():
    #print("Button clicked!")
    
    #Show an information message box
    msgbox.showinfo("Info", "welcome to COS 102 GUI App!\n")

    #Ask for user information
    result = msgbox.askyesno("Confirmation", "Dp ypu want to continue?")

    # Create the main window 
    root = tk.Tk()
    root.title("Home Page")
    root.geometry("300x100")

    # Add a label widget 
    label = tk.label(root, text="Hello Friend\n")
    label.pack()

    #Add a button widget 
    button = tk.Button(root, text="Click Me!", command=button_click)
    button.pack()

    # Styling the button widget
    button.config("red", bg="yellow")

    #Start the event loop
    root.mainloop()


    