import tkinter as tk
from tkinter.scrolledtext import *
import file_menu_functions
import edit_menu_functions
import format_menu_functions
import help_menu_functions

sgrey = "#110022"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config(bg=sgrey)

        tk.Label(
            self,
            text="Text Editor",
            fg="white",
            bg="black",
            font=("Simplified Arabic Fixed", 15, "bold"),
        ).grid()

        self.file = tk.Menubutton(
            self, relief="raised", text="File", bg=sgrey, fg="white"
        )
        self.file.menu = tk.Menu(self.file, bg=sgrey, fg="white")
        self.file["menu"] = self.file.menu

        self.edit = tk.Menubutton(
            self, relief="raised", text="Edit", bg=sgrey, fg="white"
        )
        self.edit.menu = tk.Menu(self.edit, bg=sgrey, fg="white")
        self.edit["menu"] = self.edit.menu

        self.format = tk.Menubutton(
            self, relief="raised", text="Format", bg=sgrey, fg="white"
        )
        self.format.menu = tk.Menu(self.format, bg=sgrey, fg="white")
        self.format["menu"] = self.format.menu

        self.help = tk.Menubutton(
            self, relief="raised", text="Help", bg=sgrey, fg="white"
        )
        self.help.menu = tk.Menu(self.help, bg=sgrey, fg="white")
        self.help["menu"] = self.help.menu

        self.text_box = ScrolledText(
            self,
            wrap="word",
            bg=sgrey,
            fg="white",
            font=("Helvetica", 13, "bold"),
            width=25,
            highlightthickness=0,
            insertbackground="white",
            undo=True,
        )
        self.text_box.vbar.config(troughcolor=sgrey, bg="grey")
        self.text_box.focus_set()

        file_menu_functions.main(self, self.text_box, self.file.menu)
        edit_menu_functions.main(self.text_box, self.edit.menu)
        format_menu_functions.main(self.text_box, self.format.menu)
        help_menu_functions.main(self.help.menu)
        self.file.grid(sticky="w")
        self.edit.grid(row=1, sticky="w", padx=120)
        self.format.grid(row=1, sticky="w", padx=248)
        self.help.grid(row=1, sticky="w", padx=443)
        self.text_box.grid()


Text_Editor = App()
Text_Editor.mainloop()
