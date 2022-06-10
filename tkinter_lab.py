from tkinter import *

window = Tk()
window.title("Stick Figure Drawing")
canvas = Canvas(window, width=300, height=300)
canvas.pack()
window.mainloop(30)

canvas.create_oval(100,0, 200,100)
#body
canvas.create_line(150,100, 150,225)
#arms
canvas.create_line(75,150, 225,125)
#legs
canvas.create_line(150,225, 225,300)
canvas.create_line(150,225, 75,300)