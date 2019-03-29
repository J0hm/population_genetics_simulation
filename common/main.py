import random as rand
from tkinter import *
from math import *


class Window(Frame):


     # Define settings upon initialization. 
    def __init__(self, master=None):
        
        Frame.__init__(self, master)   
            
        self.master = master

        self.init_window()

    #Creation of init_window
    def init_window(self, master=None):
             
        self.master.title("Genetics Simulation")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_exit)

        quitButton.place(x=0, y=0)

    def client_exit(self):
        sys.exit()

root = Tk()

# size window
root.geometry("600x600")

app = Window(root)
app.init_window()

root.mainloop()


