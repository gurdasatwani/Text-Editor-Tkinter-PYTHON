from datetime import datetime
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
            self.text.tag_remove(SEL, "1.0", END)
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
            self.text.tag_remove(SEL, "1.0", END)
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
            self.text.tag_remove(SEL, "1.0", END)
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
            self.text.tag_remove(SEL, "1.0", END)
        except:
            pass

    def fullDate(self):
        full_date = datetime.now()
        full_date = full_date.strftime("%B %d, %Y")
        self.text.insert(INSERT, full_date, "a")

    def addMonth(self):
        month = datetime.now()
        month = month.strftime("%B")
        self.text.insert(INSERT, month, "a")

    def addDate(self):
        date = datetime.now()
        date = date.strftime("%d")
        self.text.insert(INSERT, date, "a")

    def addYear(self):
        year = datetime.now()
        year = year.strftime("%Y")
        self.text.insert(INSERT, year, "a")

    def addDay(self):
        day = datetime.now()
        day = day.strftime("%A")
        self.text.insert(INSERT, day, "a")

    def fullTime(self):
        full_time = datetime.now()
        full_time = full_time.strftime("%H:%M:%S")
        self.text.insert(INSERT, full_time, "a")

    def addHour(self):
        hour = datetime.now()
        hour = hour.strftime("%H")
        self.text.insert(INSERT, hour, "a")

    def addMin(self):
        mint = datetime.now()
        mint = mint.strftime("%M")
        self.text.insert(INSERT, mint, "a")

    def addSec(self):
        sec = datetime.now()
        sec = sec.strftime("%S")
        self.text.insert(INSERT, sec, "a")

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
        text = " ".join(text.split())
        self.text.delete(0.0, END)
        self.text.insert(0.0, text)


def main(text, menubar):
    global formatmenu, format_functions
    formatmenu = menubar
    submenu = Menu(formatmenu, bg="#110022", fg="white")
    format_functions = Format(text)

    submenu.add_command(label="Full Date", command=format_functions.fullDate)

    submenu.add_command(label="Month", command=format_functions.addMonth)

    submenu.add_command(label="Date", command=format_functions.addDate)

    submenu.add_command(label="Year", command=format_functions.addYear)

    submenu.add_command(label="Day", command=format_functions.addDay)

    submenu.add_command(label="Full Time", command=format_functions.fullTime)

    submenu.add_command(label="Hour", command=format_functions.addHour)

    submenu.add_command(label="Minute", command=format_functions.addMin)

    submenu.add_command(label="Second", command=format_functions.addSec)

    formatmenu.add_command(label="Bold", command=format_functions.bold)

    formatmenu.add_command(label="Italic", command=format_functions.italic)

    formatmenu.add_command(label="Underline", command=format_functions.underline)

    formatmenu.add_command(label="Overstrike", command=format_functions.overstrike)

    formatmenu.add_cascade(label="Date & Time", menu=submenu)

    formatmenu.add_command(label="Capitalize", command=format_functions.capitalize)

    formatmenu.add_command(label="Read Only", command=format_functions.read_only)
