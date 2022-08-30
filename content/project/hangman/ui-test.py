from tkinter import *
from tkinter import ttk

# actual calculation performed
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

## Setting up the Main Application window
root = Tk()
root.title("Feet to Meters")

## Creating a content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
# place frame inside main application window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) 
root.columnconfigure(0, weight=1)
# frame should expand to fill any extra space if window is resized
root.rowconfigure(0, weight=1)

## Creating the entry widget
# Entry for number of feet to convert input
feet = StringVar()      # create widget
# specify parent, size, and textvariable (autoupdates this as global variable)
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # specify parent
# place in layout grid
# stick is how it should line up w.in the grid cell
feet_entry.grid(column=2, row=1, sticky=(W, E))

## Creating the remaining widget
meters = StringVar()
# display resulting number of meters calculated
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# calculate button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# static text labels
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

## Adding some polish
# adds padding to all widgets
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
# puts focus on entry widget (cursor starts there)
feet_entry.focus()
# tells Tk if user presses Return key then calculate runs
root.bind("<Return>", calculate)

root.mainloop()
