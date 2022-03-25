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

def decoder_for_list(index, list):
    return list[index]


def containerEntryfields(repeats):
   after_code = """"""
   after_code = after_code + """
from tkinter import *
def show_entry_fields():""" 
   for repeat in range(0,repeats):
      base_code = f"""

   global entry_field{repeat}
   entry_field{repeat} = e{repeat}.get() # You can use this variable later 
   print(entry_field{repeat})
         """
         
      after_code = after_code + base_code
   after_code = after_code + """
   master.destroy()
         
master = Tk()""" 
   #print(after_code)
   return after_code


def containerLabels(repeats, change_list):
   after_code = """"""

   for repeat in range(0,repeats):
      change = decoder_for_list(repeat, change_list)
      base_code = f"""
Label(master, text="{change}:").grid(row={repeat})"""       
      after_code = after_code + base_code
   #print(after_code)
   return after_code

def containerEntryfields_show(repeats):
   after_code = """"""

   for repeat in range(0,repeats):
      base_code = f"""
e{repeat} = Entry(master)"""       
      after_code = after_code + base_code
   #print(after_code)
   return after_code



def containerEntryfields_grid(repeats):
   after_code = """"""

   for repeat in range(0,repeats):
      base_code = f"""
e{repeat}.grid(row={repeat}, column=1)"""       
      after_code = after_code + base_code
      global row 
      row = repeat + 2
   after_code = after_code + f"""

Button(master, text='Quit', command=master.destroy).grid(row={row}, column=0, sticky=W, pady=4)
Button(master, text='Continue', command=show_entry_fields).grid(row={row}, column=2, sticky=W, pady=4)

mainloop()"""
   #print(after_code)
   return after_code


def make_second_file(futurePath, changes):
   with open(futurePath, 'a') as f:
      final_code = """"""

      items_len = len(changes)

      fistPhase = containerEntryfields(items_len)
      secondPhase = containerLabels(items_len, changes)
      thirdPhase = containerEntryfields_show(items_len)
      fourthPhase = containerEntryfields_grid(items_len)

      final_code = fistPhase + secondPhase + thirdPhase + fourthPhase
      f.write(final_code)
   

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

   #print(f'Your "{futureFilename}" was created!')
   make_second_file(futureFilepath, var_name)



def main(filepath, futureFilename, futureFilepath):
   stage1 = False
   stage2 = False
   stage3 = False
   chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

   filepath = Path(filepath)

   if not filepath.is_file():
      print("Error: File not found!")

   else:
      stage1 = True

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