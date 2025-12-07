import tkinter as tk
from tkinter import ttk, messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("1D Bin Packing Solver")
        self.root.geometry("1920x1080")
        self.binLabel = tk.Label(self.root, text="", font=("Courier", 16), justify="left", anchor="nw")
        self.binLabel.pack(fill="both", padx=20, pady=20)
    def drawBinFill(self,fillRate, binNumber):
        barlength = 20
        filled = int(fillRate*barlength)
        empty = barlength - filled
        bar = f"Bin {binNumber} : "
        bar += "|" + ("█"*filled) + ("-"*empty) + "| " + str(fillRate*100) + "%"
        currentText = self.binLabel["text"]
        newText = currentText + "\n" + bar
        self.binLabel.config(text=newText)
        self.root.update() 
        return bar

test = GUI()

test.drawBinFill(0.81, 1)
test.drawBinFill(0.45, 2)
test.drawBinFill(1.0, 3)

test.root.mainloop()