import random

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