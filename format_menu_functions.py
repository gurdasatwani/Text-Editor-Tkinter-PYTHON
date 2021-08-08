import time
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families


class Format:
    def __init__(self, text):
        self.text = text

    def bold(self):
        try:
            current_tag = self.text.tag_names("sel.first")
            if "bold" in current_tag:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except:
            pass

    def italic(self):
        try:
            current_tag = self.text.tag_names("sel.first")
            if "italic" in current_tag:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass

    def underline(self):
        try:
            current_tag = self.text.tag_names("sel.first")
            if "underline" in current_tag:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass

    def overstrike(self):
        try:
            current_tag = self.text.tag_names("sel.first")
            if "overstrike" in current_tag:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass

    def addDate(self):
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + "/" + month + "/" + year
        self.text.insert(INSERT, date, "a")

    def read_only(self):
        self.text.config(state="disable")
        formatmenu.delete("Read Only")
        formatmenu.add_command(label="Write", command=format_functions.write)

    def write(self):
        self.text.config(state="normal")
        formatmenu.delete("Write")
        formatmenu.add_command(label="Read Only", command=format_functions.read_only)

    def capitalize(self):
        text = self.text.get(0.0, END)
        text = text.title()
        self.text.delete(0.0, END)
        self.text.insert(0.0, text)


def main(text, menubar):
    global formatmenu, format_functions
    formatmenu = menubar
    format_functions = Format(text)

    formatmenu.add_command(label="Bold", command=format_functions.bold)

    formatmenu.add_command(label="Italic", command=format_functions.italic)

    formatmenu.add_command(label="Underline", command=format_functions.underline)

    formatmenu.add_command(label="Overstrike", command=format_functions.overstrike)

    formatmenu.add_command(label="Add Date", command=format_functions.addDate)

    formatmenu.add_command(label="Capitalize", command=format_functions.capitalize)

    formatmenu.add_command(label="Read Only", command=format_functions.read_only)
