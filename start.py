import tkinter as tk
from tkinter import ttk



class start:
    def __init__(self,root):
        #root = tk.Tk() #TODO: Delete
        root.title("Test GUI")
        # Create the frame and then pack it (don't assign the return value of pack())
        mainframe = ttk.Frame(root, padding=(5,5,5,5))  
        mainframe.pack(fill="both", expand=True)
        # Add a small demo label so the window has visible content
        demo_label = ttk.Label(mainframe, text="Hello — window is working")
        demo_label.pack(padx=8, pady=8)
            
if __name__ == "__main__":
    root = tk.Tk()  #Create the main application window
    start(root) #create an instance of simple app and pass the root window to it
    root.mainloop() #start the loop so it keeps running