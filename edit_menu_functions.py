from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class Edit:
    def __init__(self, text):
        self.clipboard = None
        self.text = text

    def copy(self):
        try:
        	select = self.text.selection_get()
        	self.clipboard = select
        	self.text.tag_remove(SEL, "1.0", END)
        except:
        	pass

    def cut(self):
        try:
            select = self.text.selection_get()
            self.clipboard = select
            self.text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass

    def paste(self):
        try:
            self.text.insert(INSERT, self.clipboard)
        except:
            pass

    def select_all(self):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(0.0, END)
        self.text.see(INSERT)

    def undo(self):
        try:
            self.text.edit_undo()
        except:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except:
            pass

    def find(self):
        self.text.tag_remove("found", "1.0", END)
        target = askstring(title="Find", prompt="Search String:")

        if target:
            index = "1.0"
            while 1:
                index = self.text.search(target, index, nocase=1, stopindex=END)
                if not index:
                    break
                last_index = "%s+%dc" % (index, len(target))
                self.text.tag_add("found", index, last_index)
                index = last_index
            self.text.tag_config("found", foreground="black", background="yellow")


def main(text, menubar):

    editmenu = menubar
    edit_functions = Edit(text)

    editmenu.add_command(label="Cut", command=edit_functions.cut)

    editmenu.add_command(label="Copy", command=edit_functions.copy)

    editmenu.add_command(label="Paste", command=edit_functions.paste)

    editmenu.add_command(label="Undo", command=edit_functions.undo)

    editmenu.add_command(label="Redo", command=edit_functions.redo)

    editmenu.add_command(label="Find", command=edit_functions.find)

    editmenu.add_command(label="Select All", command=edit_functions.select_all)
