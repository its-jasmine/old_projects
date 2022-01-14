import tkinter as tk  # imports module, and gives an alias

class Application:
    # setting values to class variables
    totalincome = 0.00
    totalexpense = 0.00
    amount_saved = 0.00
    savinggoal = 0.00

    def addexp(self):
        # move program window backwards
        self.window.lower()

        #  assigning the float value of input to variable
        self.new_expense = float(input("What is the value of the expense? (Do not include the '$') "))

        #  increments total expense value
        self.totalexpense += self.new_expense
        #  displays total expense value in a currency format
        self.expensetotal_value.config(text="$%.2f" % self.totalexpense)

        #  inserts expense in list box
        self.rect1.insert("end", ("$%.2f" % self.new_expense))

        """
        #  assigning an input to a variable
        #  self.description_expense = input("OPTIONAL: Give a brief description of what its for simply write or write'N/A' ")
        
        if self.description_expense == "N/A":
            #  inserts expense in list box and starts a new line
            self.rect1.insert("end", ("$%.2f" % self.new_expense))
        else:
            # inserts expense in list box in currency format w/ description and starts a new line
            self.rect1.insert("end", ("$%.2f" % self.new_expense) + "\t" + self.description_expense)
        """

        # move program window to the front
        self.window.attributes("-topmost", True)

    def addinc(self):
        # move program window backwards
        self.window.lower()

        #  assigning the float value of input to variable
        self.new_income = float(input("What is the value of the income? (Do not include the '$') "))

        #  increments total income value
        self.totalincome += self.new_income
        #  displays total income value in a currency format
        self.incometotal_value.config(text="$%.2f" % self.totalincome)

        #  inserts expense in list box
        self.rect2.insert("end", ("$%.2f" % self.new_income))

        """
        #  assigning an input to a variable
        self.description_income = input("OPTIONAL: Give a brief description of what its for simply write or write'N/A' ")
        
        if self.description_income == "N/A":
            #  inserts expense in list box and starts a new line
            self.rect2.insert("end", ("$%.2f" % self.new_income))
        else:
            # inserts expense in list box in currency format w/ description and starts a new line
            self.rect2.insert("end", ("$%.2f" % self.new_income) + "\t" + self.description_income)
        """

        # move program window to the front
        self.window.attributes("-topmost", True)

    def editgoal(self):
        # move program window backwards
        self.window.lower()

        #  assigns input value to variable as a string
        self.savinggoal = float(input("How much money would you like to save this year?"))
        #  displays the value in label
        self.goalsaving_value.config(text=("$%.2f" % self.savinggoal))

        # move program window to the front
        self.window.attributes("-topmost", True)

    def saving_diag(self):
        # move program window backwards
        self.window.lower()

        #  determining the amount of money saved based on the income and expenses
        self.amount_saved = self.totalincome - self.totalexpense
        # print amount saved
        print("You currently have a net balance of $%.2f" % self.amount_saved)

        # prints net balance required to achieve saving goal
        print("In order to meet your saving goal you need to have a weekly net balance of at least $%.2f." % \
              (self.savinggoal/52))
        if self.amount_saved >= (self.savinggoal/52):
            # prints message
            print("You are right on track for meeting your saving goal.")
        else:
            # prints message
            print("You will need to increase your weekly income or decrease your weekly expenses by $%.2f to meet your goal." % (self.savinggoal/52 - self.amount_saved))

    def savedata(self):
        #  retrieves the list in both list boxes
        self.expensestext = (self.rect1.get(0, "end"))
        self.incometext = (self.rect2.get(0, "end"))

        with open("conf3expenses.txt", "w") as savedexpenses:
            for items in range(0, len(self.expensestext)):
                if self.expensestext[items].find("\n") != -1:
                    #  writes each list item to the textfile
                    savedexpenses.write(self.expensestext[items])
                else:
                    #  writes each list item to the textfile w/ a newline
                    savedexpenses.write(self.expensestext[items] + "\n")
            # writes the total expenses
            savedexpenses.write("total\n")
            savedexpenses.write("$%.2f" % self.totalexpense)
        with open("conf3income.txt", "a") as savedincome:
            for items in range(0, len(self.incometext)):
                #  writes each list item to the textfile w/ a newline
                savedincome.write(self.incometext[items] + "\n")
            # writes the total income
            savedincome.write("total\n")
            savedincome.write("$%.2f" % self.totalincome)

    def printdata(self):
        #  import os
        #  os.startfile(r"C:\Users\User\Documents", "print")
        pass

    def cleardata(self):
        #  clears rext value for widgets
        self.rect1.delete(0, "end")
        self.rect2.delete(0, "end")
        self.incometotal_value.config(text="$0.00")
        self.expensetotal_value.config(text="$0.00")
        self.goalsaving_value.config(text="$0.00")

        # clears both textfiles by overwriting the files with the 'write' mode
        with open("conf3expenses.txt", "w") as expensefile:
            #  clears text file
            expensefile.write("")
        with open("conf3income.txt", "w") as incomefile:
            #  clears text file
            incomefile.write("")

    def __init__(self, window):
        # initializes the window and it's properties
        self.window = window
        self.window.configure(background="grey")  # sets background colour
        self.window.title("Budget Tracker")  # window title
        self.window.geometry("+225+100")  # sets window size and location

        #  initializes frames
        self.frame1 = tk.Frame(self.window, background="red")
        self.frame2 = tk.Frame(self.window, background="grey")
        self.frame3 = tk.Frame(self.window, background="yellow")

        #  places frames in window using grid
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1, sticky=tk.NW)
        self.frame3.grid(row=0, column=1, sticky=tk.SW)

        #  initializes widgets for frame 1
        self.expense_label = tk.Label(self.frame1, text="Expenses",font=("Times",20))
        self.addexp_but = tk.Button(self.frame1, text="Add Expense", command=self.addexp)
        self.income_label = tk.Label(self.frame1, text="Income", font=("Times", 20))
        self.addinc_but = tk.Button(self.frame1, text="Add Income", command=self.addinc)
        self.rect1 = tk.Listbox(self.frame1, width=40, height=20, fg="red")
        self.rect2 = tk.Listbox(self.frame1, width=40, height=20, fg="green")
        self.expensetotal_label = tk.Label(self.frame1, text="Total Expenses This Week", font=("Times", 15))
        self.expensetotal_value = tk.Label(self.frame1, text="$0.00", font=("Times", 15))
        self.incometotal_label = tk.Label(self.frame1, text="Total Income This Week", font=("Times", 15))
        self.incometotal_value = tk.Label(self.frame1, text="$0.00", font=("Times", 15))

        #  initializes widgets for frame 2
        self.savediag_but = tk.Button(self.frame2, text="Savings Diagnostic", font=15, command=self.saving_diag)
        self.editgoal_but = tk.Button(self.frame2, text="Edit Saving Goal", font=15, command=self.editgoal)
        self.goalsaving_label =tk.Label(self.frame2, text="This year I want to save", font=("Times", 12))
        self.goalsaving_value = tk.Label(self.frame2, text="$0.00", font=("Times", 12))

        #  initializes widgets for frame 3
        self.savedata_but = tk.Button(self.frame3, text="Save Data", font=("Times", 15), command=self.savedata)
        self.printdata_but = tk.Button(self.frame3, text="Print Data", font=("Times", 15), command=self.printdata)
        self.cleardata_but = tk.Button(self.frame3, text="Clear Data", font=("Times", 15), command=self.cleardata)

        #  places widgets in frame 1 using grid
        self.expense_label.grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)
        self.addexp_but.grid(row=0, column=0, sticky=tk.E)
        self.income_label.grid(row=0, column=2, padx=20, sticky=tk.W)
        self.addinc_but.grid(row=0, column=2, sticky=tk.E)
        self.rect1.grid(row=1, column=0, columnspan=2, padx=5)
        self.rect2.grid(row=1, column=2, columnspan=2, padx=5)
        self.expensetotal_label.grid(column=0, row=3, pady=20)
        self.expensetotal_value.grid(column=1, row=3, padx=5)
        self.incometotal_label.grid(column=2, row=3)
        self.incometotal_value.grid(column=3, row=3, padx=5)

        #  places widgets in frame 2 using grid
        self.goalsaving_label.grid(column=0, row=2, padx=30, pady=50)
        self.goalsaving_value.grid(column=1, row=2, padx=8)
        self.editgoal_but.grid(column=0, columnspan=2, row=3, padx=25)
        self.savediag_but.grid(column=0, columnspan=2, row=4, pady=50, padx=25)

        #  places widgets in frame 3 using grid
        self.savedata_but.grid(row=0, pady=10, padx=95)
        self.printdata_but.grid(row=1)
        self.cleardata_but.grid(row=2, pady=10)

        #  opens expense text file
        with open("conf3expenses.txt", "r") as expensetext:
            #  calculating number of lines in textfile (found online)
            num_lines = sum(1 for line in open('conf3expenses.txt'))
            for lines in range(0, (num_lines - 2)):
                #  reads line in text file
                expensetext_saved = expensetext.readline()
                #  inserts saved values into list box
                self.rect1.insert("end", expensetext_saved)
            #  reads last two lines
            expensetotal_saved = expensetext.readline()
            expensetotal_saved = expensetext.readline()
            if expensetotal_saved != "":
                #  displays expense total
                self.expensetotal_value.config(text=expensetotal_saved)
                #  assigns expense total to variable (last line)
                self.totalexpense = float(expensetotal_saved[1:])
        #  opens income text file
        with open("conf3income.txt", "r") as incometext:
            #  calculating number of lines in textfile (found online)
            num_lines = sum(1 for line in open('conf3income.txt'))
            for lines in range(0, (num_lines - 2)):
                # reads line in text file
                incometext_saved = incometext.readline()
                #  inserts saved values into list box
                self.rect2.insert("end", incometext_saved)
            # reads last two lines
            incometotal_saved = incometext.readline()
            incometotal_saved = incometext.readline()
            if incometotal_saved != "":
                # displays income total
                self.incometotal_value.config(text=incometotal_saved)
                #  assigns income total to variable (last line)
                self.totalincome = float(incometotal_saved[1:])


window = tk.Tk()  # creates window
# creates instance of application class and assigns to variable
run = Application(window)
window.mainloop()  # loops the window on the screen




