# Author: Lars Wisotzky

# With this script it is possible to create a Tkinter GUI from a simple 'input()'.

# Rule, only according to the following scheme can be converted:
# <variable> = input()

from tkinter import *

from pathlib import Path
import sys
import random

from __init__ import GUI_MAKER 


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


def myrandoName(chars, repeats):
    final_name = ""
    name_list = random.choices(chars,k=repeats)

    for char in name_list:
        final_name = final_name + char
    return final_name

def main(filepath, futureFilename, futureFilepath):
   
   chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

   filepath = Path(filepath)

   if not filepath.is_file():
      print("Error: File not found!")

   else:
    ownPath = sys.path[0]

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

