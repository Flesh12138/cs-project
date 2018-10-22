from tkinter import *

root = Tk()

def pick():
    import random
    import time
    while True:
        v.set(random.randint(1,100))
        root.update()
        time.sleep(1)

v = IntVar()
v.set(0)

text = Label(root, textvariable=v, font=('Calibri',20))
b1 = Button(root, text='random', command=pick)
b2 = Button(root, text='quit', command=root.quit)

text.pack()
b1.pack()
b2.pack()
mainloop()