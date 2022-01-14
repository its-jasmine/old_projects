# module imports
from tkinter import *
from random import randint


class Application:
    # assign value to variable
    perlevel_counter = 0
    elapsed_time_tally = 0
    given_up = 0

    def __init__(self, parent_window):
        self.window = parent_window  # sets parent window as an instance of the class
        self.window.geometry("+600+200")  # positions window on screen
        self.window.title("Menu")  # titles window

        # creating objects + specifying their properties
        self.but_howto = Button(self.window, text="How to Play", command = self.howto_popup)
        self.but_level1 = Button(self.window, text="Level 1", command = lambda : self.run_level_selected(9, 3))
        self.but_level2 = Button(self.window, text="Level 2", command = lambda : self.run_level_selected(12, 4))
        self.but_level3 = Button(self.window, text="Level 3", command = lambda : self.run_level_selected(18, 5))
        self.but_leaderboard = Button(self.window, text="Leaderboards", command= self.leaderboard)

        # widget gridding (positioning)
        self.but_howto.grid(row=0, column=0, columnspan=3, padx=30, sticky=NSEW)
        self.but_level1.grid(row=1, column=1)
        self.but_level2.grid(row=2, column=1)
        self.but_level3.grid(row=3, column=1)
        self.but_leaderboard.grid(row=4, column=1)

    def howto_popup(self):
        howto_popup = Tk()  # creates window
        howto_popup.geometry("+490+200")  # positions window on screen
        text_label = Label(howto_popup, text="Observe the pattern on the screen for 5 seconds.\nOnce the countdown is complete, select the correct tiles to recreate the pattern.\nGo as fast as you can to get your best score and save it to the leaderboards!\nIf you are stuck you can 'give up', however once you do this\nyou cannot save your score to the leaderboard.")
        text_label.grid()  # grids/postions widget on window
        howto_popup.mainloop()  # loops the window

    def leaderboard(self):
        leaderboard_win = Tk()  # creates window
        leaderboard_win.geometry("+500+200")  # positions window on screen
        leaderboard_win.title("Leaderboard")  # titles window

        # creates widgets and setting their properties
        lev1_label = Label(leaderboard_win, text="Level 1")
        lev2_label = Label(leaderboard_win, text="Level 2")
        lev3_label = Label(leaderboard_win, text="Level 3")
        lev1_list = Listbox(leaderboard_win, width=20, height=8)
        lev2_list = Listbox(leaderboard_win, width=20, height=8)
        lev3_list = Listbox(leaderboard_win, width=20, height=8)

        # read text file, inserts text in list box
        with open('level1.txt', "r") as level_file:
            while True:
                last_pos = level_file.tell()  # assigns postion to variable
                if level_file.readline() == "":
                    break
                level_file.seek(last_pos)  # returns cursor to last line
                lev1_list.insert(END, level_file.readline() + " - " + level_file.readline() + " seconds")  # inserts value at end of list
        with open('level2.txt', "r") as level_file:
            while True:
                last_pos = level_file.tell()  # assigns postion to variable
                if level_file.readline() == "":
                    break
                level_file.seek(last_pos)  # returns cursor to last line
                lev2_list.insert(END, level_file.readline() + " - " + level_file.readline() + " seconds")  # inserts value at end of list
        with open('level3.txt', "r") as level_file:
            while True:
                last_pos = level_file.tell()  # assigns postion to variable
                if level_file.readline() == "":
                    break
                level_file.seek(last_pos)  # returns cursor to last line
                lev3_list.insert(END, level_file.readline() + " - " + level_file.readline() + " seconds")  # inserts value at end of list

        # creating empty lists
        list_items_1 = []
        list_val_1 = []
        list_items_2 = []
        list_val_2 = []
        list_items_3 = []
        list_val_3 = []

        for items in range(0, lev1_list.size()):  # .size() retrieves the number of items in listbox
            split = lev1_list.get(items).split()  # splits sentence into list of words
            list_val_1.append(int(split[2]))  # adds numerical value to list
            list_items_1.append(lev1_list.get(items))  # adds item from listbox to list
        for items2 in range(0, lev2_list.size()):  # .size() retrieves the number of items in listbox
            split = lev2_list.get(items2).split()  # splits sentence into list of words
            list_val_2.append(int(split[2]))  # adds numerical value to list
            list_items_2.append(lev2_list.get(items2))
        for items3 in range(0, lev3_list.size()):
            split = lev3_list.get(items3).split()  # splits sentence into list of words
            list_val_3.append(int(split[2]))  # adds numerical value to list
            list_items_3.append(lev3_list.get(items3))

        # declaring the lists
        list_of_items = [list_items_1, list_items_2, list_items_3]
        list_of_val = [list_val_1, list_val_2, list_val_3]

        # sorting leaderboards
        switch = True
        while switch == True:
            switch = False
            for z in list_of_val:
                for y in range(0, len(z) - 1):
                    if z[y] > z[y + 1]:
                        switch = True
                        toobig = z.pop(y)  # removes larger value from list and assign to variable
                        z.insert(y + 1, toobig)  # reinserts value in the next spot
                        t_list = list_of_items[list_of_val.index(z)]  # assigns the corresponding item list to variable
                        toobig2 = t_list.pop(y)
                        t_list.insert(y + 1, toobig2)

        lev1_list.delete(0, END)  # clears list box
        lev2_list.delete(0, END)  # clears list box
        lev3_list.delete(0, END)  # clears list box

        # rewrites sorted in listbox
        for listy in list_of_items[0]:
            lev1_list.insert(END, listy)  # inserts value at end of list
        for listy2 in list_of_items[1]:
            lev2_list.insert(END, listy2)  # inserts value at end of list
        for listy3 in list_of_items[2]:
            lev3_list.insert(END, listy3)  # inserts value at end of list

        # gridding/positioning widgets
        lev1_label.grid(row=0, column=0)
        lev2_label.grid(row=0, column=1)
        lev3_label.grid(row=0, column=2)
        lev1_list.grid(row=1, column=0)
        lev2_list.grid(row=1, column=1)
        lev3_list.grid(row=1, column=2)

        leaderboard_win.mainloop()  # loops the window

    def run_level_selected(self, num_tiles, num_coloured):
        # assigns values to variables
        self.num_tiles = num_tiles
        self.num_coloured = num_coloured

        self.level_window = Tk() # creates window
        self.level_window.geometry("+500+85")  # positions window on screen
        self.level_window.title("Pattern Memory Game")  #titles window

        #  creating widgets and setting their properties
        if Application.perlevel_counter == 0:
            level_count_label = Label(self.level_window, text="1/3", font="25")
        elif Application.perlevel_counter == 1:
            level_count_label = Label(self.level_window, text="2/3", font="25")
        elif Application.perlevel_counter == 2:
            level_count_label = Label(self.level_window, text="3/3", font="25")
        instructions_label = Label(self.level_window, text="Look carefully at the pattern below.", font="25")
        self.check_but = Button(self.level_window, text="Check", state=DISABLED, font="20", command=self.check_pattern)
        self.timer_label = Label(self.level_window, text="6", fg="red", font="25")
        self.stopwatch_timer_label = Label(self.level_window, text="00:00", fg="purple", font="25")
        self.give_up_but = Button(self.level_window, text="I give up :(", font="25", command=self.give_up)

        # gridding/positioning the widgets
        level_count_label.grid(row=0, column=0, sticky=W)
        instructions_label.grid(row=0, column=1, columnspan=4, padx=5)
        self.timer_label.grid(row=0, column=4, padx=5, sticky=E)

        self.tiles_list = []  # creates empty list

        for num in range(0, num_tiles):
            # appends new button to list
            self.tiles_list.append(Button(self.level_window, width=12, height=5, state=DISABLED, bg="white"))

            # configures the function that runs when button is pressed, and stores current num value as the parameter
            self.tiles_list[num].config(command = lambda num = num : self.button_selection(self.tiles_list[num]))

        # list comprehension to create list with groups of 3 from the tile list
        grouped_lists = [self.tiles_list[x : x + 3] for x in range(0, len(self.tiles_list), 3)]
        x = 1
        y = 1
        # for loop to grid the tiles
        for items in grouped_lists:  # iterates through the lists in the grouped list
            for items2 in items:  # iterates through the 3 items in the lists in the grouped list
                items2.grid(column=y, row=x)  # widget gridding/positioning
                y += 1
            x += 1  # increments row value
            y = 1  # resets column value

        # gridding/postioning widgets on row below the last row of buttons
        self.stopwatch_timer_label.grid(row=x + 1, column=1)
        self.check_but.grid(row=x + 1, column=2)
        self.give_up_but.grid(row = x + 1, column=3)

        self.random_tile_list = []

        for val in range(0, self.num_coloured):
            if val == 0:
                self.random_tile_list.append(randint(0, num_tiles - 1))
            else:
                switch = True
                # appends random value (from 1 to the num of tiles) to list
                self.random_tile_list.append(randint(0, num_tiles - 1))
                while switch == True:
                    switch = False
                    for val2 in self.random_tile_list[:-1]:
                        if self.random_tile_list[- 1] == val2:
                            switch = True
                            # assigns new value to last item
                            self.random_tile_list[-1] = randint(0, num_tiles - 1)

            for x in self.random_tile_list:
                self.tiles_list[x].config(bg="blue")  # changes background colour to blue

        self.countdown()  # calls countdown function

        self.level_window.after(5000, lambda : self.clear_tiles())  # runs anonymous form of function after 5 seconds

        self.level_window.after(5000, lambda : self.stopwatch())   # runs anonymous form of function after 5 seconds

        self.level_window.mainloop()

    def countdown(self):
        current_time = int(self.timer_label.cget("text"))  # retrieves text value from label
        if current_time > 0:
            self.timer_label.config(text=str(current_time - 1))  # reconfigures label text to decremented value
            self.level_window.after(1000, lambda : self.countdown())  # reruns countdown function after 10000 milisecs

    def stopwatch(self):
        # splits text value in label and assigns to variable
        current_time = (self.stopwatch_timer_label.cget("text")).split(":")
        current_time_1 = int(current_time[0])
        current_time_1_string = current_time[0]
        current_time_2 = int(current_time[1])

        if current_time_2 < 59:
            if current_time_2 < 9:
                self.stopwatch_timer_label.config(text="%s:0%i" % (current_time_1_string, current_time_2 + 1))  # reconfigures the text with incremented values
            else:
                self.stopwatch_timer_label.config(text="%s:%i" % (current_time_1_string, current_time_2 + 1))  # reconfigures the text with incremented values
        else:
            if current_time_1 < 9:
                self.stopwatch_timer_label.config(text="0%i:00" % (current_time_1 + 1))  # reconfigures the text with incremented values
            else:
                self.stopwatch_timer_label.config(text="%i:00" % (current_time_1 + 1))  # reconfigures the text with incremented values

        self.level_window.after(1000, lambda: self.stopwatch())  # reruns stopwatch function after 10000 milisecs

    def clear_tiles(self):
        # for x in range(1, 10):
        for x in range(0, self.num_tiles):
            # returns button to original colour + makes it active again
            self.tiles_list[x].config(bg="white", state=NORMAL)
        self.check_but.config(state=NORMAL)  # returns button to active state

    def button_selection(self, tile):
        if tile.cget("bg") == "blue":
            tile.config(bg="white")  # changes tile colour to white
        else:
            tile.config(bg="blue")  # changes tile colour to blue

    def check_pattern(self):
        num_correct = 0
        not_selected_tally = 0
        #  checks if buttons in pattern were selected
        for items in self.random_tile_list:
            if self.tiles_list[items].cget("bg") == "blue":
                num_correct += 1  # increments value

        for items2 in self.tiles_list:
            if items2.cget("bg") == "white":
                not_selected = True  # sets the value to True, since it is white (not selected)
                for items3 in self.random_tile_list:
                    if self.tiles_list.index(items2) == items3:
                        not_selected = False  # sets the value to False, since this tile is part of the pattern
                    if not_selected == True:
                        not_selected_tally += 1  # increments tally
                        break

        if num_correct == self.num_coloured and not_selected_tally == self.num_tiles - self.num_coloured :
            elapsed_time = self.stopwatch_timer_label.cget("text").split(":")  # splits string at the :
            Application.elapsed_time_tally += int(elapsed_time[0]) * 60 + int(elapsed_time[1])  # assigns elapsed time in seconds to class variable

            if Application.perlevel_counter < 2:
                Application.perlevel_counter += 1  # increments pattern counter
                self.level_window.destroy()  # closes the window that is currently open
                self.run_level_selected(self.num_tiles, self.num_coloured)  # calls the function
            else:
                Application.perlevel_counter = 0  # resets pattern counter after third pattern
                self.level_window.destroy()  # closes the window that is currently open
                self.completed()

    def give_up(self):
        Application.given_up += 1
        if Application.perlevel_counter < 2:
            Application.perlevel_counter += 1  # increments pattern counter
            self.level_window.destroy()  # closes the window that is currently open
            self.run_level_selected(self.num_tiles, self.num_coloured)  # calls the function
        else:
            Application.perlevel_counter == 0  # resets pattern counter after third pattern
            self.level_window.destroy()  # closes the window that is currently open
            self.completed()

    def completed(self):
        completed_window = Tk()  # creates window
        completed_window.geometry("+500+200")  # positions window on screen

        # creates widgets and sets their properties
        completed_elapsed_time_label = Label(completed_window, font="20")
        save_time_but = Button(completed_window, text="Save to Leaderboard", command = self.input_popup)
        return_but = Button(completed_window, text="Return to Menu", command = lambda : completed_window.destroy())

        # determines what level was played
        if self.num_tiles == 9:
            level = 1
        elif self.num_tiles == 12:
            level = 2
        elif self.num_tiles == 18:
            level = 3

        if Application.given_up > 0:
            save_time_but.config(state=DISABLED)  # disables button
            Application.given_up = 0  # resets variable value
            # configures text value of label
            completed_elapsed_time_label.config(text="You completed level %i in %i seconds." % (level, Application.elapsed_time_tally))
            Application.elapsed_time_tally = 0  # resets elapsed time tally

        # configures text value of label
        completed_elapsed_time_label.config(text="You completed level %i in %i seconds." % (level, Application.elapsed_time_tally))

        # grids/positions widgets
        completed_elapsed_time_label.grid(row=0, column=0, columnspan=2)
        save_time_but.grid(row=1, column=0)
        return_but.grid(row=1, column=1)

        completed_window.mainloop()

    def input_popup(self):
        self.input_popup_win = Tk()  # creates window
        self.input_popup_win.geometry("+600+200")

        # creates widgets and set their properties
        enter_name_label = Label(self.input_popup_win, text="Enter your name below.")
        self.entry_box = Entry(self.input_popup_win)
        enter_but = Button(self.input_popup_win, text="Enter", command=self.save_to_file)

        # grids/positions widgets
        enter_name_label.grid()
        self.entry_box.grid()
        enter_but.grid()

        self.input_popup_win.mainloop()  # loops the window on the screen

    def save_to_file(self):
        self.user_input = self.entry_box.get()  # retrieves the value in the text box
        self.entry_box.config(text="")  # clears entry box

        self.input_popup_win.destroy()  # closes window

        # assigns values to variables
        """
        list_r_files = [open('level1.txt', "r"), open('level2.txt', "r"), open('level3.txt', "r")]
        list_w_files = [open('level1.txt', "w"), open('level2.txt', "w"), open('level3.txt', "w")]
        """
        list_a_files = [open('level1.txt', "a"), open('level2.txt', "a"), open('level3.txt', "a")]

        #  assigns value to variable based on the level played
        if self.num_tiles == 9:
            index = 0
        elif self.num_tiles == 12:
            index = 1
        elif self.num_tiles == 18:
            index = 2
        """
        # checks if user name already exists, writes the user name and time in text file and closes after
        with list_r_files[index] as check_lev:
            text = iter(check_lev.readlines())  # assigns the text in file as iterable to variable
        with list_w_files[index] as edit_lev:
            for lines in text:
                if self.user_input + "\n" != lines:
                    edit_lev.write(lines)  # rewrites the line to text file
                else:
                    next(text)  # skips a line in the text
            edit_lev.write(self.user_input + "\n" + str(Application.elapsed_time_tally) + "\n")  # writes to file
        """
        with list_a_files[index] as edit_lev:
            edit_lev.write(self.user_input + "\n" + str(Application.elapsed_time_tally) + "\n")  # writes to file

        Application.elapsed_time_tally = 0  # resets elapsed time tally


window = Tk()  # creates window
run = Application(window)  # runs instance of class
window.mainloop()  # loops the display of the window on screen

