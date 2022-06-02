from tkinter import *
from functools import partial 
import random

class Start:
    def __init__(self, parent):
         
        self.var_starting_balance = IntVar()

        button_font = "Arial 12 bold"
        
        # GUI to get starting balance and stakes 
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play",
                                  bg="#808080", fg="white", font=button_font, 
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=5, pady=10)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        button_font = "Arial 12 bold"
        
        # disable help button
        partner.help_button.config(state=DISABLED)
        
        #sets up child window (ie: help box)
        self.help_box = Toplevel()        
       
        # If user press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
       
        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300,)
        self.help_frame.grid()
       
        # Set up Help Heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                font =button_font)
        self.how_heading.grid(row=0)                        
        
        # Help text (Label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, wrap=250)   
        self.help_text.grid(row=1)                        
       
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", 
                                  width=10, 
                           command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, padx=10, pady=10)                   
        
    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    Start(root)
    root.mainloop()