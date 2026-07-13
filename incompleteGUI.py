import tkinter as tk
from tkinter import PhotoImage, Tk, ttk

class Test:

    def __init__(self, root):
        #root = tk.Tk() #TODO
        self.root = root
        root.configure(background='#0D031B')
        root.title("FINALTEST")

    def createNbuttons(self, soilFrame: ttk.Frame, vertical: bool,text: list[str]):
        "Creates buttons and stores them in a class attribute. Takes a frame, a boolean for vertical or horizontal layout, and a list of button texts."
        self.auto_buttons = []
        if vertical:
            for i, button_text in enumerate(text): #StackOverflow, thank you
                autoButton = ttk.Button(soilFrame, text=button_text)
                autoButton.grid(column=1, row=i)
                self.auto_buttons.append(autoButton)
        else:
            for i, button_text in enumerate(text): #StackOverflow, thank you
                autoButton = ttk.Button(soilFrame, text=button_text)
                autoButton.grid(column=i, row=1)
                self.auto_buttons.append(autoButton)
    
# [#][][]
        leftFrame = ttk.Frame(root
    ).grid(column=1, sticky="NSE")
        #leftLabel = ttk.Label(leftFrame,text="1,2.1,2.").grid(column=1,row=2)
        listButtons = ["Inventory", "Graphs", "Warnings"]



    # How you would modify it in another class method:
    def changeNbuttons(self):
        # ttk buttons use styles for colors, but for basic config:
        for button in self.auto_buttons:
            button.config(text="Changed")
        


# [][#]][]
        centerFrame = ttk.Frame(root
    ).grid(column=2, sticky="NSEW")
        centerLabel = ttk.Label(centerFrame,text="Existes?").grid(column=2,row=1)
    
# [][][#]
        rightFrame = ttk.Frame(root
    ).grid(column=3, sticky="NSW")
        rightLabel = ttk.Label(rightFrame,text="Porfavor, funciona").grid(column=3,row=0)
        
if __name__ == "__main__":
    root = tk.Tk()
    Test(root)
    root.mainloop()