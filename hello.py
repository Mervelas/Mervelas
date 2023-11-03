import time
from tkinter import *
import tkinter as tk
import webbrowser
from tkcalendar import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Button
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno
from time import strftime
from tkinter import Label, Tk
import mysql.connector as mysql
from tkinter import Label, Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import io
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib
import random
import os
import tempfile
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class Rapport:
    def __init__(self, root):
        self.root = root
        self.root.title("Rapport Stock ")
        self.root.iconbitmap(r"Icones/shopping_cart2.ico")
        self.root.geometry("1156x513+200+152")
        self.root.focus_force()
        self.root.resizable(False, False)
        self.root.configure(bg="#f3f3f2")


##Frame TITRE
        self.frametitre = Frame(self.root, bg="#009fd4", width=1150, height=50)
        self.frametitre.place(x=0, y=0)

        lb = tk.Label(self.frametitre, text="GESTION DES RAPPORTS MENSUEL", font=("Book Antiqua", 20, "bold"), bg="#009fd4", fg="#f8f8f2")
        lb.place(x=10, y=10)

        



       
       

        













if __name__ == "__main__":
    root = Tk()
    obj = Rapport(root)
    root.mainloop()
