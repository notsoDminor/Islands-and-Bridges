import tkinter as tk
import random

win = tk.Tk()
canvas = tk.Canvas(win, width = 430, height = 450, bg = "Bisque")
canvas.pack()

voda = []
zem = []
piczem = tk.PhotoImage(file ="images/ostrov3.png")
picvoda = tk.PhotoImage(file ="images/ostrov0.png")
obrazky = [tk.PhotoImage(file = "images/ostrov_kruh0.png"), tk.PhotoImage(file ="images/ostrov_kruh1.png")]
mosty = [tk.PhotoImage(file = "images/ostrov1.png"), tk.PhotoImage(file ="images/ostrov2.png")]
xobr = 50
yobr = 50
switcher = 0
score = 0

def click_switcher(e):
    global switcher
    if canvas.itemcget("switcher", "image") == "pyimage3":
        canvas.itemconfig("switcher", image = obrazky[1])
        switcher = 1
    elif canvas.itemcget("switcher", "image") == "pyimage4":
        canvas.itemconfig("switcher", image = obrazky[0])
        switcher = 0

def checker(e):
    global switcher, score
    if switcher == 0:
        x = (e.x//50)*50
        y = (e.y//50)*50
        ID = canvas.find_withtag("current")[0]
        canvas.delete(ID)
        canvas.create_image(x, y, image = mosty[0], anchor = "nw", tags = "bridge")
        score += 10
    elif switcher == 1:
        x = (e.x//50)*50
        y = (e.y//50)*50
        ID = canvas.find_withtag("current")[0]
        canvas.delete(ID)
        canvas.create_image(x, y, image = piczem, anchor = "nw")
        score += 50
    text.config(text = score)


def counter(e):
    global score
    text.config(text = score)

def rotate(e):
    global switcher
    if switcher == 0:
        if canvas.itemcget("current", "image") == "pyimage5":
            canvas.itemconfig("current", image = mosty[1])
        elif canvas.itemcget("current", "image") == "pyimage6":
            canvas.itemconfig("current", image = mosty[0])

def create_screen():
    global zem, score, text
    m = random.randint(4, 6)
    n = random.randint(3, 9)
    for stlpec in range(n):
        for riadok in range(m):
            temp = random.randint(0, 5)
            if temp == 1:
                tempz = canvas.create_image(riadok * xobr, stlpec * yobr, image = piczem, anchor = "nw")
                zem.append(tempz)
            else:
                tempv = canvas.create_image(riadok * xobr, stlpec * yobr, image = picvoda, anchor = "nw", tags = "water")
                voda.append(tempv)
    canvas.create_image(420, 10, anchor = "ne", image = obrazky[0], tags = "switcher")
    text = tk.Label(text = score, bg = "Bisque", width = 0, height = 0)
    text.place(x = 310, y = yobr / 2 - 10)
    text.config(font = ("System", 20), fg = "Black")

create_screen()
canvas.tag_bind("switcher", "<Button-1>", click_switcher)
canvas.tag_bind("water", "<Button-1>", checker)
canvas.tag_bind("bridge", "<Button-1>", rotate)
canvas.bind("<Button-1>", counter)

win.mainloop()
