from tkinter import *
global root
root = Tk()
text = Text(root)
text.insert(INSERT, 'Memory\n')
text.pack()

with open('output.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        text.insert(INSERT, line)

root.after(10000, lambda: root.destroy())


root.mainloop()
