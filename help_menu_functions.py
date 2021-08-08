from tkinter import *
from tkinter.messagebox import *
import webbrowser


class Help:
    def about(self):
        showinfo(
            title="CREDIT",
            message="This Is A Simple Text Editor Created By\nArjun Satwani..",
        )

    def insta(self):
        webbrowser.open_new_tab("https://www.instagram.com/arjuunsatwani/")

    def github(self):
        webbrowser.open_new_tab("https://github.com/arjunsatwani")


def main(menubar):

    helpmenu = menubar

    help_functions = Help()

    helpmenu.add_command(label="Instagram", command=help_functions.insta)

    helpmenu.add_command(label="GitHub", command=help_functions.github)

    helpmenu.add_command(label="About", command=help_functions.about)