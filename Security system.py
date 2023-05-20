# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 16:49:53 2022

@author: ALIENWARE
"""

from tkinter import *
import os 
from tkinter import messagebox


def session():
    screen6 = Toplevel(screen)
    screen6.title("session")
    screen6.geometry("500x500")
    Label(screen6, text = "Welcome", font = ("Airstrike", 20)).pack()
    

def login_success():
    session()
    
def deletepage2():
    screen4.destroy()
    
def password_not_found():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Incorrect")
    screen4.geometry("150x150")
    Label(screen4, text = "Password Incorrect").pack()
    Button(screen4, text = "OK", command = deletepage2).pack()
    

def deletepage3():
    screen5.destroy()

def username_unavailable():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Username Unavailable")
    screen5.geometry("150x150")
    Label(screen5, text = "Username Unavailable").pack()
    Button(screen5, text = "OK", command = deletepage3).pack()   

    
def register_newuser():          #Storing new entry for password and username
    username_info = username.get()      #Obtaining and storing username
    password_info = password.get()      #Obtaining and storing password
    if (username_info =="" or password_info ==""):
        messagebox.showwarning(title = "Error", message = "Enter username and password")
    elif(len(password_info) < 7):
        messagebox.showwarning(title = "Error", message = "Password must be equal to or more than 7 characters")
    else:
        storagefile = open(username_info, "w")     #Creating a file to store username and password
        storagefile.write(username_info+"\n")       #write the username into the file with the "\n" to leave a line between username and password
        storagefile.write(password_info)    #write the password into the file
        storagefile.close()
   
        

    #To remove the username and password out of the entry points after entering them"
    username_entry.delete(0, END)
    password_entry.delete(0, END)


    Label(screen1, text = "Registration Successful", fg = "green", font = ("Vivaldi", 15)).pack()
    

    
    
def register():             #Creating the register account page
    global screen1          #make screen1 accessible in all parts
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x400")
    
    #Making pairs of usernames and password accessible by globalizing them
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()      #String Variable for username entry
    password = StringVar()      #String variable for password entry
          
        
    
    #Creating entry points for username and password details
    Label(screen1, text = "Please enter details below * ", font = ("Stencil", 13)).pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ", font = ("Monotype Corsiva", 11)).pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Password * ", font = ("Monotype Corsiva", 11)).pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()

    Button(screen1, text = "Register", activebackground= "Red", font = ("Stencil", 10), width = "10", height = "2", command =register_newuser).pack()





    
def login_verify():     #Command to access credentials
    username1 = username_verify.get()   #creating access points to already entered username and password
    password1 = password_verify.get()

        
    if (username1 =="" or password1 ==""):
        messagebox.showwarning(title = "Error", message = "Enter username and password") 
    else:
        username_entry2.delete (0, END)     #deleting entries of username and password after button is pressed
        password_entry2.delete (0, END)
    
    #accessing directory for username and password file
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file_1 = open(username1, "r")       #access the file as read only
        verify = file_1.read().splitlines()     #splitlines to ignore the spaces between username and password
        if (password1 in verify):
            messagebox.showwarning(title = "Success", message = "Login Successful")
            login_success()
        else:
            messagebox.showwarning(title = "Error", message = "Password Incorrect")
    else:
        username_unavailable()
    
    
   
def login():
    global screen2
    screen2 = Toplevel(screen)      #creating a dialog box for the main screen for login
    screen2.title("Login")
    screen2.geometry("300x400")
    
    #Creating title for login page
    Label(screen2, text = "Please enter details below to login * ", font = ("Britannic Bold", 13)).pack()
    Label(screen2, text = "").pack()
    
    #Making username and password accessible
    global username_verify
    global password_verify
    
    #String Variables to record username and password for entry
    username_verify = StringVar()
    password_verify = StringVar()
    
    #Making username and password entries accessible
    global username_entry2
    global password_entry2
    
    #Entry points for username and password
    Label(screen2, text = "Username * ", font = ("Monotype Corsiva", 11)).pack()
    username_entry2 = Entry(screen2, textvariable = username_verify)
    username_entry2.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ", font = ("Monotype Corsiva", 11)).pack()
    password_entry2 = Entry(screen2, textvariable = password_verify)
    password_entry2.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", activebackground= "Blue", font = ("Stencil", 10), width = "10", height = "2", command = login_verify).pack()
    
    

def mainscreen():           #Home Screen Creation
    global screen
    screen = Tk()
    screen.geometry("300x500")
    screen.title("Access Page")
    Label(text = "Login", bg = "Gray", width = "200", height = "2", font = ("Old English Text MT", 20)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30", activebackground="Cyan", height = "2", bg = "White", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30", activebackground="Cyan", height = "2", bg = "White", command = register).pack()
    
    screen.mainloop()
mainscreen()
    
    