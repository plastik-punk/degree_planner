from tkinter import *

# creates window with title bar, minimize, maximize and close buttons
root=Tk()
root.title("Degree Planner")
root.geometry("500x500")

# Label widget, child of root window (Label can display text, icon or image)
hello_world = Label(root, text="Hello World!")
# makes Label visible
    # hello_world.pack()
# geometry manager for labels that keeps label in the desired location, default 0,0
hello_world.grid()

def clicked():
    # changes text of hello_world label
    hello_world.configure(text="Hi yourself!")

btn = Button(root, text="Say Hi!", fg="red", command=clicked)
btn.grid(column=1, row=0)


def run():
    # renderloop
    root.mainloop()
