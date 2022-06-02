from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        self.var_starting_balance = IntVar()

        button_font = "Arial 12 bold"

        # GUI to get starting balance and stakes 
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                               " (between $5 and $50) in the box "
                                               "below. Then choose the stakes."
                                               " The higher the stakes, "
                                               "the more you can win!",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry box (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)


        # self.start_amount_entry = Entry(self.start_frame, font="Arial 19 bold")
        # self.start_amount_entry.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_buttons = Button(self.entry_error_frame,
                                        font="Arial 14 bold",
                                        text="Add  Funds",
                                        command=self.check_funds)
        self.add_funds_buttons.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange low stakes button...
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Yellow medium stakes button...
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, padx=5, pady=10)

        # Green high stakes button...
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, pady=10)

        # Disable all stakes buttons at start
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # amount_error label (set to blank at start)
        self.amount_error_label = Label(self.start_frame, font="Arial 10 italic",
                                          text="error goes here",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.amount_error_label.grid(row=4)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()
        
        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # Change background to white (for testing purposes) ...
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disable all stakes buttons in case user changes mind and 
        # decreases amount entered.
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is $5 " 
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in " \
                                        "this game is $50"
            
            
            elif starting_balance >= 15:
                # enable all buttons 
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)
            elif starting_balance >= 10:
                # enable low and medium stakes buttons 
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
            else:
                self.low_stakes_button.config(state=NORMAL)

            
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            # set starting balance to amount entered by user
            self.var_starting_balance.set(starting_balance)

    def to_game(self,stakes):

        button_font = "Arial 12 bold"

        # retrieve starting balance
        starting_balance = self.var_starting_balance.get()

        Game(self, stakes, starting_balance)

        # hide start up window
        self.start_frame.destroy()

         # Help Button
        self.help_button = Button(self.start_frame, text="How/Rules",
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



class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables 
        self.balance = IntVar()
        # Set starting balance to amount entered by user at start of game 
        self.balance.set(starting_balance)

        # Get value of stakes (use it as a multiplier when calculating winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding statistics
        self.round_stats_list = []
        
        # GUI Setup
        self.game_box = Toplevel()
       
        # If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading row 
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open"
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"  # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prizel_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prizel_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.box_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=1, columnspan = 3, pady = 10)

        # bind button to <enter> (users can push enter to reveal the boxes)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        # self.play_button.grid(row=0)

        # Balance Label (row 4)
        start_text = "Game Cost: ${} \n "" \nHow much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                   text=start_text, wrap=300,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white", command=self.help)
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()
        
        round_winnings = 0
        prizes = []
        backgrounds = []
        stats_prizes = []

        for item in range(0, 3):
            prize_num = random.randint(1,100)
            
            if 0 < prize_num <= 5:
                prize_list = "gold\n(${})".format(5* stakes_multiplier)
                prize = "gold"
                back_color = "#CEA935"  # Gold colour
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize_list = "silver\n(${})".format(2* stakes_multiplier)
                prize = "silver"
                back_color = "#B7B7B5"  # Silver colour 
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize_list = "copper\n(${})".format(1* stakes_multiplier)
                prize = "copper"
                back_color = "#BC7F61" # copper colour 
                round_winnings += stakes_multiplier
            else:
                prize_list = "lead\n($0)"
                prize = "lead"
                back_color = "#595E71"

            prizes.append(prize_list)
            backgrounds.append(back_color)
            stats_prizes.append(prize_list)

        # Display prizes & edit background...
        self.prizel_label.config(text=prizes[0], bg=backgrounds[0])
        
        self.prize2_label.config(text=prizes[1], bg=backgrounds[1])
        
        self.prize3_label.config(text=prizes[2], bg=backgrounds[2])

        # Deduct cost of the game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                        round_winnings,
                                                        current_balance)

        # Add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${} \n" \
                        "Payback: ${} | Current Balance: "\
                        "${}".format(stats_prizes[0], stats_prizes[1],
                                     stats_prizes[2],
                                     5 * stakes_multiplier,round_winnings,
                                     current_balance)
        self.round_stats_list.append(round_summary)
        print("\n\n",self.round_stats_list)
        
        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)
    
    def to_quit(self):
        root.destroy()

    def help(self):
        print("you asked for help")
        get_help = Help(self)

        help_text = "These are the instructions.  There is quite a bit of content here.  Wrapping might need to be invovled"

        get_help.help_text.configure(text=help_text)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    Start(root)
    root.mainloop()

        


        