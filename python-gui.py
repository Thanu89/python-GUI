# imports
from tkinter import *
from tkinter import messagebox
import sqlite3
# ------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Creating a connection to the school_life database.
db = sqlite3.connect('school_life.db')
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL);')
db.commit()
db.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Class for creating the log in window


class login_window:

    # __init__ function that creates the window.
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.widgets()

    # Allows the user to attempt to log into their account.
    def login(self):
        db = sqlite3.connect('school_life.db')
        c = db.cursor()

        user_search = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(user_search[(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n You have logged in!'
            self.head['pady'] = 150
        else:
            ms.showerror("User details not found! Please try again!")

    # A function that allows the user to create a new account.
    def create_new_user(self):
        db = sqlite3.connect('school_life.db')
        c = db.cursor()

        user_search = ('SELECT * FROM user WHERE username = ?')
        c.execute(user_search[(self.new_username.get())])
        result = c.fetchall()

        if result:
            ms.showerror('Sorry! This username has already been taken!')

        else:
            ms.showinfo('Your account has been created successfully!')
            self.log()

        add_user = 'INSERT INTO user(username, password) VALUES (?,?)'
        c.execute(add_user, [(self.new_username.get()), (self.new_password.get())])
        db.commit()

    # Creates the widget for the Log in window.
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Log In'
        self.logf.pack()

    # Creates the widget for the create account window.
    def cr(self):
        self.new_username.set('')
        self.new_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Puts the widgets on the screen
    def widgets(self):
        # self.head = Label(self.master, text='Log In', pady=10)
        # self.head.pack()
        # self.logf = Frame(self.master, padx=10, pady=10)
        # Label(self.logf, text='Username: ', pady=5, padx=5).grid(sticky=W)
        # Entry(self.logf, textvariable=self.username, bd=5).grid(row=0, column=1)
        # Label(self.logf, text='Password: ', pady=5, padx=5).grid(sticky=W)
        # Entry(self.logf, textvariable=self.password, bd=5, show='*').grid(row=1, column=1)
        # Button(self.logf, text='Create Account', bd=3, padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        # self.logf.pack()

        # self.crf = Frame(self.master, padx=10, pady=10)
        # Label(self.crf, text='Username: ', pady=5, padx=5).grid(sticky=W)
        # Entry(self.crf, textvariable=self.new_username, bd=5).grid(row=0, column=1)
        # Label(self.crf, text='Password: ', pady=5, padx=5).grid(sticky=W)
        # Entry(self.crf, textvariable=self.new_password, bd=5, show='*').grid(row=1, column=1)
        # Button(self.crf, text='Create Account', bd=3, pady=5, padx=5, command=self.create_new_user).grid()
        # Button(self.crf, text='Go To Log In Page', bd=3, padx=5, pady=5, command=self.login).grid(row=2, column=1)

        self.head = Label(self.master, text='LOGIN', pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', pady=5, padx=5).grid(sticky='W')
        Entry(self.logf, textvariable=self.username, bd=5,).grid(row=0, column=1)
        Label(self.logf, text='Password: ', pady=5, padx=5).grid(sticky='W')
        Entry(self.logf, textvariable=self.password, bd=5, show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', padx=5, pady=5, command=self.cr).grid(row=2, column=2)

        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', pady=5, padx=5).grid(sticky='W')
        Entry(self.crf, textvariable=self.new_username, bd=5,).grid(row=0, column=1)
        Label(self.crf, text='Password: ', pady=5, padx=5).grid(sticky='W')
        Entry(self.crf, textvariable=self.new_password, bd=5, show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', padx=5, pady=5, command=self.create_new_user).grid()
        Button(self.crf, text='Go to Login', padx=5, pady=5, command=self.log).grid(row=2, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title('Login Form')
    login_window(root)
    root.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------------------------ #

# I have gotten the window to work, but cannot get the creation of user to work as of yet, which I will manage over christmas.
