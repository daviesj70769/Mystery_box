from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import re


class Start:
    def __init__(self, parent):
        # GUI for Flag Quiz
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Heading
        self.Quiz_box_label = Label(self.start_frame, text="Flag Quiz",
                                    font="Arial 19 bold")
        self.Quiz_box_label.grid(row=0, column=0)

        # Quiz text
        self.start_text = Label(self.start_frame, text="Welcome to my Flag Quiz "
                                                       "i have got a large variety of "
                                                       "flag questions and i hope you enjoy the quiz, "
                                                       "as it is my first ever peice of code that i have done "
                                                       "majority of by myself.\n\n"
                                                       "press play when ready!",
                                justify=LEFT, width=40, wrap=250, font="Arial 12")
        self.start_text.grid(row=1)

        # Help and Play button (row 3)
        self.help_export_frame = Frame(self.start_frame)
        self.help_export_frame.grid(row=2, pady=15, padx=15)

        self.play_button = Button(self.help_export_frame, text="Play",
                                  bg="midnight blue", fg="white", font="Arial 15 bold", command=self.mode)
        self.play_button.grid(row=0, column=0, padx=10, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                  font="Arial 15 bold",
                                  bg="maroon", fg="white", command=self.help)
        self.help_button.grid(row=0, column=1, padx=2)

    def mode(self):
        print("Choose a mode!")
        choose_mode = Mode(self)

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.config


class Help:
    def __init__(self, partner):
        button_font = "Arial 12 bold"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If user press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, )
        self.help_frame.grid()

        # Set up Help Heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font=button_font)
        self.how_heading.grid(row=0)

        help_text = "1. Pressing play will take you to the mode choosing area.\n\n" \
                    "2. When choosing a mode it is good to note that there is 10 questions " \
                    "in the easy mode, 20 questions in the medium mode and 30 in the hard mode.\n\n" \
                    "3. Once you have choosen your mode/amount of questions, you will then be put straight " \
                    "into the quiz answering the questions.\n\n" \
                    "4. While in the quiz you can quit at anytime but your progress will be lost when doing so.\n\n" \
                    "5. At the end of the quiz you will have an option to either exit/close the quiz or you can go to" \
                    " the history button and you will be able to see your stats and you will be able to export them if you" \
                    " feel the need to save your score.\n\n"

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
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


class Mode:
    def __init__(self, partner):
        # GUI Setup
        self.mode_box = Toplevel()

        self.mode_frame = Frame(self.mode_box, width=300)
        self.mode_frame.grid()

        # If user press cross at top, closes mode selection
        self.mode_box.protocol('WM_DELETE_WINDOW', partial(self.to_quit, partner))

        # Set up Help Heading (row 0)
        self.how_heading = Label(self.mode_frame, text="Choose a mode",
                                 font="arial 18 bold")
        self.how_heading.grid(row=0)

        # Easy mode button
        self.easy_button = Button(self.mode_frame, text="Easy",
                                  font="arial 15 bold", width=10, padx=10, pady=10, bg="Dark Green", fg="white",
                                  command=self.mode_frame)
        self.easy_button.grid(row=1, pady=10)

        # Medium mode button
        self.Medium_button = Button(self.mode_frame, text="Medium",
                                    font="arial 15 bold", width=10, padx=10, pady=10, bg="Purple", fg="white",
                                    command=self.mode_frame)
        self.Medium_button.grid(row=2, pady=10)

        # Hard mode button
        self.Hard_button = Button(self.mode_frame, text="Hard",
                                  font="arial 15 bold", width=10, padx=10, pady=10, bg="Hot Pink", fg="white",
                                  command=self.mode_frame)
        self.Hard_button.grid(row=3, pady=10)

        # Quit Button
        self.quit_button = Button(self.mode_box, text="Quit", fg="white",
                                  bg="Black", font="Arial 15 bold", width=10,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=4, pady=10)

    def close_mode(self, partner):
        partner.mode_button.config(state=NORMAL)
        self.mode_box.destroy()

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flag Quiz")
    Start(root)
    root.mainloop()