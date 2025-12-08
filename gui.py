import tkinter as tk
from tkinter import ttk, messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("1D Bin Packing Solver")
        self.root.geometry("1920x1080")
        #Graph frame
        self.binGraphFrame = tk.Frame(self.root)
        self.binGraphFrame.pack(expand=True)
        #Left graph for backtracking
        self.leftFrame = tk.Frame(self.binGraphFrame)
        self.leftFrame.pack(side="left", padx=20)
        self.binGraphLeft = tk.Text(self.leftFrame, font=("Courier", 16),width=45)
        self.binGraphLeft.pack(side="left",padx=20, pady=20)
        self.leftLabel = tk.Label(self.leftFrame, text="Algorithm 1", font=("Courier", 16))
        #Right graph for cultural algorithm
        self.rightFrame = tk.Frame(self.binGraphFrame)
        self.rightFrame.pack(side="left", padx=20)
        self.rightLabel = tk.Label(self.rightFrame, text="Algorithm 2", font=("Arial", 16))
        self.binGraphRight = tk.Text(self.binGraphFrame, font=("Courier", 16),width=45)
        self.binGraphRight.pack(side="left",padx=20, pady=20)
    def drawBinFillLeft(self,fillRate, binNumber):
        barlength = 20
        filled = int(fillRate*barlength)
        empty = barlength - filled
        bar = f"Bin {binNumber} : "
        bar += "|" + ("█"*filled) + ("-"*empty) + "| " + str(fillRate*100) + "%"
        newText = "\n" + bar
        self.binGraphLeft.config(state="normal")
        self.binGraphLeft.insert("end", newText + "\n")
        self.binGraphLeft.config(state="disabled")
        self.binGraphLeft.see("end")
        return bar
    def drawBinFillRight(self,fillRate, binNumber):
        barlength = 20
        filled = int(fillRate*barlength)
        empty = barlength - filled
        bar = f"Bin {binNumber} : "
        bar += "|" + ("█"*filled) + ("-"*empty) + "| " + str(fillRate*100) + "%"
        newText = "\n" + bar
        self.binGraphRight.config(state="normal")
        self.binGraphRight.insert("end", newText + "\n")
        self.binGraphRight.config(state="disabled")
        self.binGraphRight.see("end")
        return bar

test = GUI()

# Container for all controls (instructions + inputs + dropdown)
topFrame = tk.Frame(test.root)
topFrame.pack(side="top", pady=20)

# Instructions
instructions = tk.Label(
    topFrame,
    text=("1D Bin Packing Solver\nEnter the minimum and maximum item sizes, then choose an algorithm to run.\nThe solver will pack items into bins of fixed capacity and show the bin usage."),
    font=("Helvetica", 14),
    justify="center")
instructions.pack(pady=10)

# Min/Max inputs
inputFrame = tk.Frame(topFrame)
inputFrame.pack(pady=10)

tk.Label(inputFrame, text="Min Item Size:").grid(row=0,column=0, padx=10)
entMinSize =tk.Entry(inputFrame, width=10)
entMinSize.grid(row=0, column=1,padx=10)
tk.Label(inputFrame, text="Max Item Size:").grid(row=0,column=2, padx=10)
entMaxSize = tk.Entry(inputFrame, width=10)
entMaxSize.grid(row=0, column=3,padx=10)

# Dropdown menu for algorithms
algoFrame = tk.Frame(topFrame)
algoFrame.pack(pady=10)
tk.Label(algoFrame,text="Select Algorithm:").pack()

# variable to hold selected algorithm
selectedAlgo = tk.StringVar(test.root)
selectedAlgo.set("Backtracking Algorithm")  # default
algoOptions = ["Backtracking Algorithm","Cultural Algorithm","Both"] # List of options

# remember last selection
lastSelection = {"value": selectedAlgo.get()}

def whenAlgoChange(choice):
    # choice is the new value selected from the dropdown
    if choice == lastSelection["value"]:
        return # the same option is selected again, nothing will change
    # update selection value
    lastSelection["value"] = choice
    selectedAlgo.set(choice)

algoDropdown = ttk.OptionMenu(
    algoFrame,
    selectedAlgo,
    selectedAlgo.get(), # default shown value
    *algoOptions,
    command=whenAlgoChange)
algoDropdown.pack(pady=5)

test.root.mainloop()