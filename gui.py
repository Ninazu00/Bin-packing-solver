import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("1D Bin Packing Solver")

tk.Label(root, text="Algorithm:")
algo_var = tk.StringVar()
algo_dropdown = ttk.Combobox(root, textvariable=algo_var, values=["Backtracking", "Cultural"])