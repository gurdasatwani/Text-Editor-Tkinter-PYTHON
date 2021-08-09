# Main Modules

import os
import tkinter as tk
import webbrowser
from tkinter.font import Font
from tkinter.filedialog import *
from datetime import datetime
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

sgrey = "#110022"

# App Class


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.menubar = tk.Menu(self, bg=sgrey, fg="white")
        self.config(menu=self.menubar, bg=sgrey)

        self.lframe = tk.LabelFrame(
            self, text="Text Editor", padx=5, pady=5, bg=sgrey, fg="white"
        )
        self.lframe.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewns")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.lframe.columnconfigure(0, weight=1)
        self.lframe.rowconfigure(0, weight=1)

        self.txtbox = ScrolledText(
            self.lframe,
            width=40,
            height=10,
            undo=True,
            selectbackground="grey",
            bg=sgrey,
            fg="white",
            highlightthickness=0,
            insertbackground="white",
            wrap='word'
        )
        self.txtbox.vbar.config(troughcolor=sgrey, bg="grey")
        self.txtbox.grid(row=0, column=0, sticky="ewns")
        self.txtbox.focus_set()

        File(self, self.txtbox, self.menubar)
        Edit(self.txtbox, self.menubar)
        Format(self.txtbox, self.menubar)
        Help(self.menubar)


# File Class


class File:
    def __init__(self, root, txtbox, menubar):
        self.root = root
        self.txtbox = txtbox
        self.menubar = menubar
        self.filename = "Untitled.txt"
        self.filestate = "Ready"
        self.main()

    def new(self):
        if (
            str(self.txtbox.get(0.0, "end")).isspace()
            or self.filename != "Untitled.txt"
            and self.filestate == "Saved"
        ):
            pass
        else:
            ask = askyesno(title="Save", message="Do You Want To Save This File?")
            if ask == True:
                self.save()
        self.filename = "Untitled.txt"
        self.filestate = "Ready"
        self.txtbox.delete(0.0, "end")

    def open(self):
        try:
            file = askopenfile(mode="r")
            self.filename = file.name
            text = file.read()
            self.txtbox.delete(0.0, "end")
            self.txtbox.insert(0.0, text)
            file.close()
            self.filestate = "Saved"
        except:
            showerror(title="Oops!", message="Unable To Open File...")

    def save(self):
        if self.filename == "Untitled.txt" and self.filestate == "Ready":
            save = asksaveasfile(
                mode="w",
                defaultextension=".txt",
                initialfile=os.path.basename(str(self.filename)),
            )
        else:
            save = open(self.filename, mode="w")
        text = self.txtbox.get(0.0, "end")
        try:
            save.write(text)
            save.close()
            self.filestate = "Saved"
            showinfo(title="Saved", message="File Was Saved")
        except:
            showerror(title="Oops!", message="Unable To Save File...")

    def save_as(self):
        ask = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt")
        text = self.txtbox.get(0.0, "end")
        try:
            save = open(ask, mode="w")
            save.write(text)
            save.close()
            showinfo(title="Saved", message="File Was Saved")
            self.filestate = "Saved"
            self.filename = ask
        except:
            showerror(title="Oops!", message="Unable To Save File...")

    def delete(self):
        try:
            ask = askyesno(title="Delete", message="Are You Sure You Want To Delete?")
            if ask == True:
                os.remove(self.filename)
                self.txtbox.delete(0.0, "end")
                showinfo(title="Deleted", message="The File Was Deleted.")
                self.filename = "Untitled.txt"
                self.filestate = "Ready"

        except:
            showerror(title="Oops!", message="The File Doesn't Exist..")

    def Exit(self):
        ask = askyesno(title="Exit", message="Are You Sure You Want To Exit?")
        if ask == True:
            self.root.destroy()

    def main(self):
        file = tk.Menu(self.menubar, bg=sgrey, fg="white")
        file.add_command(label="New", command=lambda: File.new(self))
        file.add_command(label="Open", command=lambda: File.open(self))
        file.add_command(label="Save", command=lambda: File.save(self))
        file.add_command(label="Save As", command=lambda: File.save_as(self))
        file.add_command(label="Delete", command=lambda: File.delete(self))
        file.add_command(label="Exit", command=lambda: File.Exit(self))

        self.menubar.add_cascade(label="File", menu=file)


# Edit Class


class Edit:
    def __init__(self, txtbox, menubar):
        self.txtbox = txtbox
        self.menubar = menubar
        self.clipboard = None
        self.main()

    def cut(self):
        try:
            select = self.txtbox.selection_get()
            self.clipboard = select
            self.txtbox.delete(SEL_FIRST, SEL_LAST)
        except:
            pass

    def copy(self):
        try:
            select = self.txtbox.selection_get()
            self.clipboard = select
            self.txtbox.tag_remove(SEL, "1.0", END)
        except:
            pass

    def paste(self):
        try:
            self.txtbox.insert(INSERT, self.clipboard)
        except:
            pass

    def undo(self):
        try:
            self.txtbox.edit_undo()
        except:
            pass

    def redo(self):
        try:
            self.txtbox.edit_redo()
        except:
            pass

    def find(self):
        self.txtbox.tag_remove("found", "1.0", END)
        target = askstring(title="Find", prompt="Search String:")

        if target:
            index = "1.0"
            while 1:
                index = self.txtbox.search(target, index, nocase=1, stopindex=END)
                if not index:
                    break
                last_index = "%s+%dc" % (index, len(target))
                self.txtbox.tag_add("found", index, last_index)
                index = last_index
            self.txtbox.tag_config("found", foreground="black", background="yellow")

    def select_all(self):
        self.txtbox.tag_add(SEL, "1.0", END)
        self.txtbox.mark_set(0.0, END)
        self.txtbox.see(INSERT)

    def main(self):
        editmenu = tk.Menu(self.menubar, bg=sgrey, fg="white")
        editmenu.add_command(label="Cut", command=lambda: Edit.cut(self))
        editmenu.add_command(label="Copy", command=lambda: Edit.copy(self))
        editmenu.add_command(label="Paste", command=lambda: Edit.paste(self))
        editmenu.add_command(label="Undo", command=lambda: Edit.undo(self))
        editmenu.add_command(label="Redo", command=lambda: Edit.redo(self))
        editmenu.add_command(label="Find", command=lambda: Edit.find(self))
        editmenu.add_command(label="Select All", command=lambda: Edit.select_all(self))

        self.menubar.add_cascade(label="Edit", menu=editmenu)


# Format Class


class Format:
    def __init__(self, txtbox, menubar):
        self.txtbox = txtbox
        self.menubar = menubar
        self.main()

    def bold(self):
        try:
            current_tag = self.txtbox.tag_names("sel.first")
            if "bold" in current_tag:
                self.txtbox.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.txtbox.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.txtbox, self.txtbox.cget("font"))
                bold_font.configure(weight="bold")
                self.txtbox.tag_configure("bold", font=bold_font)
            self.txtbox.tag_remove(SEL, "1.0", END)
        except:
            pass

    def italic(self):
        try:
            current_tag = self.txtbox.tag_names("sel.first")
            if "italic" in current_tag:
                self.txtbox.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.txtbox.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.txtbox, self.txtbox.cget("font"))
                italic_font.configure(slant="italic")
                self.txtbox.tag_configure("italic", font=italic_font)
            self.txtbox.tag_remove(SEL, "1.0", END)
        except:
            pass

    def underline(self):
        try:
            current_tag = self.txtbox.tag_names("sel.first")
            if "underline" in current_tag:
                self.txtbox.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.txtbox.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.txtbox, self.txtbox.cget("font"))
                underline_font.configure(underline=1)
                self.txtbox.tag_configure("underline", font=underline_font)
            self.txtbox.tag_remove(SEL, "1.0", END)
        except:
            pass

    def overstrike(self):
        try:
            current_tag = self.txtbox.tag_names("sel.first")
            if "overstrike" in current_tag:
                self.txtbox.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.txtbox.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.txtbox, self.txtbox.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.txtbox.tag_configure("overstrike", font=overstrike_font)
            self.txtbox.tag_remove(SEL, "1.0", END)
        except:
            pass

    def capitalize(self):
        text = self.txtbox.get(0.0, END)
        text = text.title()
        text = " ".join(text.split())
        self.txtbox.delete(0.0, END)
        self.txtbox.insert(0.0, text)

    def fullDate(self):
        full_date = datetime.now()
        full_date = full_date.strftime("%B %d, %Y")
        self.txtbox.insert(INSERT, full_date, "a")

    def addMonth(self):
        month = datetime.now()
        month = month.strftime("%B")
        self.txtbox.insert(INSERT, month, "a")

    def addDate(self):
        date = datetime.now()
        date = date.strftime("%d")
        self.txtbox.insert(INSERT, date, "a")

    def addYear(self):
        year = datetime.now()
        year = year.strftime("%Y")
        self.txtbox.insert(INSERT, year, "a")

    def addDay(self):
        day = datetime.now()
        day = day.strftime("%A")
        self.txtbox.insert(INSERT, day, "a")

    def fullTime(self):
        full_time = datetime.now()
        full_time = full_time.strftime("%H:%M:%S")
        self.txtbox.insert(INSERT, full_time, "a")

    def addHour(self):
        hour = datetime.now()
        hour = hour.strftime("%H")
        self.txtbox.insert(INSERT, hour, "a")

    def addMin(self):
        mint = datetime.now()
        mint = mint.strftime("%M")
        self.txtbox.insert(INSERT, mint, "a")

    def addSec(self):
        sec = datetime.now()
        sec = sec.strftime("%S")
        self.txtbox.insert(INSERT, sec, "a")

    def main(self):
        formatmenu = tk.Menu(self.menubar, bg=sgrey, fg="white")
        submenu = tk.Menu(formatmenu, bg=sgrey, fg="white")
        submenu2 = tk.Menu(formatmenu, bg=sgrey, fg="white")

        font = Font(family="Arial", size=13)
        self.txtbox.config(font=font)

        for i in range(13, 31):
            submenu2.add_command(label=str(i), command=lambda i=i: font.config(size=i))

        submenu.add_command(label="Full Date", command=lambda: Format.fullDate(self))
        submenu.add_command(label="Month", command=lambda: Format.addMonth(self))
        submenu.add_command(label="Date", command=lambda: Format.addDate(self))
        submenu.add_command(label="Year", command=lambda: Format.addYear(self))
        submenu.add_command(label="Day", command=lambda: Format.addDay(self))
        submenu.add_command(label="Full Time", command=lambda: Format.fullTime(self))
        submenu.add_command(label="Hour", command=lambda: Format.addHour(self))
        submenu.add_command(label="Minute", command=lambda: Format.addMin(self))
        submenu.add_command(label="Second", command=lambda: Format.addSec(self))

        formatmenu.add_command(label="Bold", command=lambda: Format.bold(self))
        formatmenu.add_command(label="Italic", command=lambda: Format.italic(self))
        formatmenu.add_cascade(label="Size", menu=submenu2)
        formatmenu.add_command(
            label="Underline", command=lambda: Format.underline(self)
        )
        formatmenu.add_command(
            label="Overstrike", command=lambda: Format.overstrike(self)
        )
        formatmenu.add_command(
            label="Capitalize", command=lambda: Format.capitalize(self)
        )
        formatmenu.add_cascade(label="Date & Time", menu=submenu)

        def write():
            self.txtbox.config(state="normal")
            formatmenu.delete("Write")
            formatmenu.add_command(label="Read Only", command=read_only)

        def read_only():
            self.txtbox.config(state="disable")
            formatmenu.delete("Read Only")
            formatmenu.add_command(label="Write", command=write)

        formatmenu.add_command(label="Read Only", command=read_only)

        self.menubar.add_cascade(label="Format", menu=formatmenu)


# Help Class


class Help:
    def __init__(self, menubar):
        self.menubar = menubar
        self.main()

    def insta(self):
        webbrowser.open_new_tab("https://www.instagram.com/arjuunsatwani/")

    def github(self):
        webbrowser.open_new_tab("https://github.com/arjunsatwani")

    def about(self):
        showinfo(
            title="CREDIT",
            message="This Is A Simple Text Editor Created By\nArjun Satwani..",
        )

    def main(self):
        helpmenu = tk.Menu(self.menubar, bg=sgrey, fg="white")
        helpmenu.add_command(label="Instagram", command=lambda: Help.insta(self))
        helpmenu.add_command(label="GitHub", command=lambda: Help.github(self))
        helpmenu.add_command(label="About", command=lambda: Help.about(self))

        self.menubar.add_cascade(label="Help", menu=helpmenu)


a = App()
a.mainloop()
