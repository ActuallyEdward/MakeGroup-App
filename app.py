import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
import tkinter.messagebox
from pandastable import Table, TableModel

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu,tearoff= "off")
        "need to add command for save"
        fileMenu.add_command(label="Save") 
        fileMenu.add_separator()
        fileMenu.add_command(label="Load", command = self.OpenFile)
        menu.add_cascade(label="File", menu=fileMenu)
    
    


    def OpenFile(self):
        tkinter.messagebox.showinfo("Message","Warning: Only .csv file or .txt file allowed!")
        "This program allows for csv file, and tex file"
        filepath = filedialog.askopenfilename()

        if (filepath.endswith('.csv')):
            df = pd.read_csv(filepath)
            displayData(df)
            tkinter.messagebox.showinfo("Message","File loaded")
            
            "Tested using the print function, the loaded file is fine"
        elif (filepath.endswith('.txt')):
            "Ask for user's input on the seperator"
            input = simpledialog.askstring(title= "Query", prompt="What's the seperator?:")
            df = pd.read_csv(filepath, sep=input)
            displayData(df)
            tkinter.messagebox.showinfo("Message","File loaded")
            
            "Tested using the print function, the loaded file is fine"

def displayData(df):
        f = Frame(frame1)
        f.pack(fill=BOTH,expand=1)
        pt = Table(f, dataframe=df,showtoolbar=False, showstatusbar=False)
        pt.show()   
    
        
def conf(event):
    h = int(1/2*root.winfo_height())
    w = int(1/2*root.winfo_width())
    notebook.config(height=h,width=w)   




root = Tk()
app = Window(root)
root.wm_title("MakeGroup App")
root.geometry("500x500")
"NoteBook for logs"
notebook = ttk.Notebook(root)
notebook.pack(pady=0, expand=True)
notebook.grid(row=0,column=0,sticky="w")

# create frames
frame1 = ttk.Frame(notebook, width=200, height=200)
frame2 = ttk.Frame(notebook, width=200, height=200)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

root.bind("<Configure>",conf)

# add frames to notebook

notebook.add(frame1, text='Data')
notebook.add(frame2, text='Similarity')

root.mainloop()

