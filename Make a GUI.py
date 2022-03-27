# Author: Lars Wisotzky

# With this script it is possible to create a Tkinter GUI from a simple 'input()'.

# Rule, only according to the following scheme can be converted:
# <variable> = input()



from tkinter import *
from pathlib import Path
import sys
import random


ownPath = sys.path[0]

def myrandoName(chars, repeats):
    final_name = ""
    name_list = random.choices(chars,k=repeats)

    for char in name_list:
        final_name = final_name + char
    return final_name


class GUI_MAKER:

    def __init__(self, futurePath, changes):
        
        self.futurePath = futurePath
        self.changes = changes
        
        with open(self.futurePath, 'a') as f:
            self.final_code = """"""

            self.items_len = len(self.changes)

            self.fistPhase = self.containerEntryfields(self.items_len)
            self.secondPhase = self.containerLabels(self.items_len, self.changes)
            self.thirdPhase = self.containerEntryfields_show(self.items_len)
            self.fourthPhase = self.containerEntryfields_grid(self.items_len)

            self.final_code = self.fistPhase + self.secondPhase + self.thirdPhase + self.fourthPhase
            f.write(self.final_code)
        
    def myrandoName(self, chars, repeats):
        self.final_name = ""
        self.name_list = random.choices(chars,k=repeats)

        for char in self.name_list:
            self.final_name = self.final_name + char
        return self.final_name

    def decoder_for_list(self, index, list):
        return list[index]


    def containerEntryfields(self, repeats):
        self.after_code = """"""
        self.after_code = self.after_code + """
from tkinter import *
def show_entry_fields():""" 
        for repeat in range(0,repeats):
            self.base_code = f"""

    global entry_field{repeat}
    entry_field{repeat} = e{repeat}.get() # You can use this variable later 
    print(entry_field{repeat})
                """
                
            self.after_code = self.after_code + self.base_code
        self.after_code = self.after_code + """
    master.destroy()
                
master = Tk()""" 
        #print(after_code)
        return self.after_code


    def containerLabels(self, repeats, change_list):
        self.after_code = """"""

        for repeat in range(0,repeats):
            self.change = self.decoder_for_list(repeat, change_list)
            self.base_code = f"""
Label(master, text="{self.change}:").grid(row={repeat})"""       
            self.after_code = self.after_code + self.base_code
        #print(after_code)
        return self.after_code

    def containerEntryfields_show(self, repeats):
        self.after_code = """"""

        for repeat in range(0,repeats):
            self.base_code = f"""
e{repeat} = Entry(master)"""       
            self.after_code = self.after_code + self.base_code
        #print(after_code)
        return self.after_code



    def containerEntryfields_grid(self, repeats):
        self.after_code = """"""

        for repeat in range(0,repeats):
            self.base_code = f"""
e{repeat}.grid(row={repeat}, column=1)"""       
            self.after_code = self.after_code + self.base_code
 
            self.row = repeat + 2
        self.after_code = self.after_code + f"""

Button(master, text='Quit', command=master.destroy).grid(row={self.row}, column=0, sticky=W, pady=4)
Button(master, text='Continue', command=show_entry_fields).grid(row={self.row}, column=2, sticky=W, pady=4)

mainloop()"""
        #print(after_code)
        return self.after_code
   


def file_scan(filepath, futureFilepath):
   times = 0
   var_name = []
   with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.strip()
            list_code = data.split()
            for index, code in enumerate(list_code):
               if code == 'input()':
                  code_before_index = index - 1
                  code_before = list_code[code_before_index]
                  if code_before == '=':
                     code_before_index = code_before_index - 1
                     name_of_inp = list_code[code_before_index]
                     times = times + 1
                     var_name.append(name_of_inp)

   GUI_MAKER(futureFilepath, var_name)


def main(filepath, futureFilename, futureFilepath):
   
   chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

   filepath = Path(filepath)

   if not filepath.is_file():
      print("Error: File not found!")

   else:

      if futureFilename == "" and futureFilepath == "":
         futPath = ownPath
         futName = myrandoName(chars, 5) + '.py'
         total_path = futPath + "\makeGui_" + futName

      elif futureFilename == "" and not futureFilepath == "":
         futName = myrandoName(chars, 5) + '.py'
         total_path = futureFilepath + "\makeGui_" + futName

      elif not futureFilename == "" and futureFilepath == "":
         futPath = ownPath
         total_path = futPath + f"\{futureFilename}"  + '.py'

      elif not futureFilename == "" and not futureFilepath == "":
         total_path = futureFilepath + f"\{futureFilename}"  + '.py'

      else:
         print("Something went wrong!")
         quit

      file_scan(filepath, total_path)
      print(f"Your File successfully created! Path: {total_path}")
         

# Own Interface

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
