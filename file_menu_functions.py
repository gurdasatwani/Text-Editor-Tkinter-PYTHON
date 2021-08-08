from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys, os


class File:
    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root

    def new_file(self):
        self.filename = "Untitled.txt"
        self.text.delete(0.0, END)

    def save(self):
        try:
            self.filename = asksaveasfilename(defaultextension=".txt")
            text = self.text.get(0.0, END)
            save = open(file=self.filename, mode="w")
            save.write(text)
            save.close()
            showinfo(title="Saved", message="File Was Saved")
        except:
            showerror(title="Oops!", message="Unable To Save File...")

    def save_as(self):
        save = asksaveasfile(mode="w", defaultextension=".txt")
        text = self.text.get(0.0, END)
        try:
            save.write(text.rstrip())
            save.close()
            showinfo(title="Saved", message="File Was Saved")
        except:
            showerror(title="Oops!", message="Unable To Save File...")

    def open(self):
        try:
            file = askopenfile(mode="r")
            self.filename = file.name
            text = file.read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, text)
        except:
            pass

    def delete(self):
        try:
            ask = askyesno(title="Delete", message="Are You Sure You Want To Delete?")
            if ask == True:
                os.remove(self.filename)
                showinfo(title="Deleted", message="The File Was Deleted.")
        except:
            showerror(title="Oops!", message="The File Doesn't Exist..")

    def Exit(self):
        ask = askyesno(title="Exit", message="Are You Sure You Want To Exit?")
        if ask == True:
            self.root.destroy()


def main(root, text, menubar):

    filemenu = menubar
    file_functions = File(text, root)

    filemenu.add_command(label="New", command=file_functions.new_file)

    filemenu.add_command(label="Open", command=file_functions.open)

    filemenu.add_command(label="Save", command=file_functions.save)

    filemenu.add_command(label="Save As", command=file_functions.save_as)

    filemenu.add_command(label="Delete", command=file_functions.delete)

    filemenu.add_command(label="Exit", command=file_functions.Exit)
