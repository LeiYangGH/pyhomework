from tkinter import *
from tkinter.ttk import *

TEMPLATE = "Name: {0}\nHeight: {1:.2f} m\nHorns: {2}"

class Blork(object):
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        

class BlorkGui(object):
    """Defines the Blork Interface"""
##    def order():
##        print(1)
    def __init__(self, window, blorks):
        """Setup the label and button on given window"""
        self.blorks = blorks
        self.window = window
        box = ["Blorkstien", "Chewblorka", "Jack", "Jeff", "Lily"]
        combo = Combobox(window, value = box)
        combo.grid(row = 0, column = 0)
        
        #button = Button(self.window, text = 'View details', command = order)
        button = Button(self.window, text = 'View details')
        button.grid(row = 0, column = 1)
        
        label = Label(self.window, text = "Press 'View details'")
        label.grid(row = 1, column = 0)
        

        
    

def main():
    """Set up the GUI and run it."""    
    blorks = {"Jeff": Blork("Jeff", 1.6),
              "Lily": Blork("Lily", 1.111111),
              "Jack": Blork("Jack", 1.89),
              "Chewblorka": Blork("Chewblorka", 3.14, True),
              "Blorkstien": Blork("Blorkstien", 0.856, True)}
    window = Tk()
    blork_gui = BlorkGui(window, blorks)
    window.mainloop()

main()
