#Name: SONAM CHOPHEL
#Student Number: 10600541

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
import json

# The choice method from the random is selected in order to choose random games for choose for me method
from random import choice


class App:
    def __init__(self, root):
        # setting window
        root.title("Game Finder")

        # setting background image
        self.bg = tk.PhotoImage(file='images/bg.png')
        # icon setup
        self.icon = tk.PhotoImage(file='images/icon.png')
        root.iconphoto(False, self.icon)

        # Show image using label
        background = tk.Label(root, image=self.bg)
        background.place(x=0, y=0)

        # dumping json data into the self.data var
        # opening file by using with keyword will close the file after its operation
        try:
            with open('data.txt') as fptr:
                self.data = json.load(fptr)
        except (FileNotFoundError, TypeError, ValueError):
            root.destroy
            return
        # available games for randomly choosing for the user
        self.games_available = [data for data in self.data]
        # Keeping the records of the games that are displayed on found side
        self.included = []

        # The header of the game with its own frame
        header_frame = tk.Frame(root, border=2)
        header_frame.pack(side=TOP, pady=30)
        GLabel_907 = tk.Label(header_frame)
        GLabel_907["bg"] = "#000"
        # GLabel_907["disabledforeground"] = "#000000"
        ft = tkFont.Font(family='Monospace', size=18)
        GLabel_907["font"] = ft
        GLabel_907["fg"] = "white"
        GLabel_907["justify"] = "center"
        GLabel_907["text"] = "Constraints"
        GLabel_907.pack(side=TOP)
        ###

        ##### Frames Defined Here #####

        # The content frame holds the label_frame and entry_frame
        content_frame = tk.Frame(root, border=2, bg="cyan")
        content_frame.pack(side=TOP, padx=20)

        # This frame contains only the label widgets
        label_frame = tk.Frame(content_frame, bg="blue")
        label_frame.pack(side=LEFT)

        # This frame contains the entry widgets
        entry_frame = tk.Frame(content_frame, bg="yellow")
        entry_frame.pack(side=RIGHT)

        # This frame contains the submit and suggestion button
        # add bg property if you want bg color
        mid_frame = tk.Frame(root, border=2, bg="black")
        mid_frame.pack(side=TOP, pady=50)

        # This frame contains the last matching results
        self.last_frame = tk.Frame(root, border=2, bg='black', pady=20
                                   )
        self.last_frame.pack(side=TOP)

        ##### Frames End #####

        # 1st row
        GLabel_773 = tk.Label(label_frame)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_773["font"] = ft
        GLabel_773["fg"] = "#ffffff"
        GLabel_773["justify"] = "center"
        GLabel_773["text"] = "Number of players:"
        GLabel_773.pack(side=TOP, pady=10, padx=10)

        self.player_count = tk.Entry(entry_frame)
        self.player_count["borderwidth"] = "1px"
        self.player_count["relief"] = "solid"
        self.player_count.pack(side=TOP, pady=10, padx=10)
        ###

        # 2nd row
        GLabel_780 = tk.Label(label_frame)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_780["font"] = ft
        GLabel_780["fg"] = "#ffffff"
        GLabel_780["justify"] = "center"
        GLabel_780["text"] = "Time Available (mins):"
        GLabel_780.pack(side=TOP, pady=10, padx=10)

        self.time_limit = tk.Entry(entry_frame)
        self.time_limit["borderwidth"] = "1px"
        self.time_limit["relief"] = "solid"
        self.time_limit.pack(side=TOP, pady=10, padx=10)
        ###

        # 3rd Row
        GLabel_482 = tk.Label(label_frame)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_482["font"] = ft
        GLabel_482["fg"] = "#ffffff"
        GLabel_482["justify"] = "center"
        GLabel_482["text"] = "Age of Youngest Player: "
        GLabel_482.pack(side=TOP, padx=10, pady=10)
        # entry
        self.young_age_field = tk.Entry(entry_frame)
        self.young_age_field["borderwidth"] = "1px"
        self.young_age_field["relief"] = "solid"
        self.young_age_field.pack(side=TOP, padx=10, pady=10)
        ###

        # Fourth row for submit and suggestion button
        GButton_20 = tk.Button(mid_frame)
        # GButton_20["bg"] = "white"
        ft = tkFont.Font(family='Consolas', size=10)
        GButton_20["font"] = ft
        GButton_20["fg"] = "#000000"
        GButton_20["justify"] = "center"
        GButton_20["text"] = "Submit"
        GButton_20["command"] = self.findGames
        GButton_20.pack(side=TOP, pady=10)

        # The function randomly chooses one of the available options

        def chooseForMe():
            if len(self.games_available) > 0:
                choosenGame = choice(self.games_available)
                button = tk.Button(self.last_frame)
                button['text'] = choosenGame['name']
                self.included.append(choosenGame['name'])
                button.pack(side=TOP, pady=10)
                # Function to show the game details when clicked

                def showDetails():
                    tk.messagebox.showinfo(f'{choosenGame["name"]}', f"{choosenGame['name']}\nPlayers: {str(choosenGame['min_players'])} - {str(choosenGame['max_players'])}\
                        \nDuration: {str(choosenGame['duration'])}\nMinimum Age: {str(choosenGame['min_age'])}")

                # removing games to avoid duplication
                toRemove = []
                for i in range(len(self.games_available)):
                    if self.games_available[i]['name'] == choosenGame['name']:
                        toRemove.append(i)
                if len(toRemove) > 0:
                    for index in toRemove:
                        self.games_available.pop(index)
                button['command'] = showDetails
            else:
                tk.messagebox.showerror("Empty", "There are no results left")

        # The button for the random choice "Choose for me"
        GButton_625 = tk.Button(mid_frame)
        # GButton_625["bg"] = "white"
        ft = tkFont.Font(family='Times', size=10)
        GButton_625["font"] = ft
        GButton_625["fg"] = "#000000"
        GButton_625["justify"] = "center"
        GButton_625["text"] = "Choose For Me"
        GButton_625["command"] = chooseForMe
        GButton_625.pack(side=BOTTOM, pady=10)
        ###

    def findGames(self):

        ### Results views ###

        # Converting the input values to integer
        try:
            number_of_players = int(self.player_count.get())
            time_available = int(self.time_limit.get())
            youngest_age = int(self.young_age_field.get())
        except ValueError:
            tk.messagebox.showerror('Error', 'Invalid criteria specified')
        else:
            # Searching
            found = list()
            for game in self.games_available:
                if game['min_players'] <= number_of_players <= game['max_players'] and game['duration'] <= time_available and game['min_age'] <= youngest_age:
                    if game['name'] not in self.included:
                        found.append(game)
                        self.included.append(game['name'])
                        # removing the item from the available games
                        for i in range(len(self.games_available)):
                            if self.games_available[i]['name'] == game['name']:
                                self.games_available.pop(i)

        ### Matching Games Heading ###
            GLabel_111 = tk.Label(self.last_frame)
            ft = tkFont.Font(family='Tahoma', size=20,)
            GLabel_111["font"] = ft
            GLabel_111["fg"] = "blue"
            GLabel_111["bg"] = "black"
            GLabel_111["justify"] = "center"
            GLabel_111["text"] = "Matching Games:"
            GLabel_111.pack(side=TOP, padx=10, pady=10)

            if len(found) < 1:
                notFound = tk.Label(self.last_frame)
                ft = tkFont.Font(family='Tahoma', size=15,)
                notFound["font"] = ft
                notFound["fg"] = "#ff0000"
                notFound["justify"] = "center"
                notFound["text"] = "No Matching Games ⚠"
                notFound.pack(side=TOP, padx=10, pady=10)
            else:
                if len(found) > 1:
                    tk.messagebox.showinfo(
                        'Total Matches', f'{str(len(found))} out of {str(len(self.data))} games matched the search')
                else:
                    tk.messagebox.showinfo(
                        'Total Matches', f'{str(len(found))} out of {str(len(self.data))} game matched the search')

                for item in found:
                    # setting up the message dialog box for the buttons
                    def showDetails():
                        tk.messagebox.showinfo(f'{item["name"]}', f"{item['name']}\nPlayers: {str(item['min_players'])} - {str(item['max_players'])}\
                        \nDuration: {str(item['duration'])}\nMinimum Age: {str(item['min_age'])}")
                    # Button for the item found
                    button = tk.Button(self.last_frame)
                    button["bg"] = "white"
                    ft = tkFont.Font(family='Consolas', size=10)
                    button["font"] = ft
                    button["fg"] = "#000000"
                    button["justify"] = "center"
                    button["text"] = item['name']
                    button["command"] = showDetails
                    button.pack(side=TOP, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
