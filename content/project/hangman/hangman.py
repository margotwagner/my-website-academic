from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):

        # main application window
        root.title("Hangman Helper")

        # content frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # correct guess input
        self.correct = StringVar()
        correct_entry = ttk.Entry(mainframe, width=7, textvariable=self.correct)
        correct_entry.grid(column=2, row=1, sticky=(W, E))

        # incorrect guess input
        self.incorrect = StringVar()
        incorrect_entry = ttk.Entry(mainframe, width=7, textvariable=self.correct)
        incorrect_entry.grid(column=2, row=2, sticky=(W, E))


        # static text labels
        ttk.Label(mainframe, text="correct guesses").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="incorrect guesses").grid(column=1, row=2, sticky=E)
        #ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root = Tk()
FeetToMeters(root)
root.mainloop()
