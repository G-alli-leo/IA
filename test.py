from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
def l_text(parameter: str):
    l.configure(text="txt")
l.bind('<Enter>', l_text("Moved mouse inside"))
l.bind('<Leave>', l_text("Moved mouse outside"))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<2>', lambda e: l.configure(text='Clicked THAT mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked third mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text=f'third button drag to {e.x},{e.y}'))
root.mainloop()