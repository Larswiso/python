from tkinter import *

from main import main

def tinterface():

    def show_entry_fields():
        Filepath = e1.get()   
        futureFilename = e2.get()  
        futureFilepath = e3.get()

        main(Filepath, futureFilename, futureFilepath)
        quit()


    master = Tk()
    Label(master, text="Filepath:").grid(row=0)
    Label(master, text="Future Filename:").grid(row=1)
    Label(master, text="Future Filepath:").grid(row=2)


    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Continue', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

    mainloop()

tinterface()