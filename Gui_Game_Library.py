#!usr/bin/python3
#Austin Andrews
#02/10/2020

'''Gui Version of the game library app'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

class Screen(tk.Frame):

    current = 0

    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()    


class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text ="Game Library",
                                  font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, 
                            sticky = "news")
        
        self.btn_add = tk.Button(self, text="Add", font = BUTTON_FONT, command = self.go_add)
        self.btn_add.grid(row = 1, column = 1)
        
        
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT, command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 1)
        

        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT, command = self.go_search)
        self.btn_search.grid(row = 3, column = 1)
        
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT, command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 1,)
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT, command = self.go_save)
        self.btn_save.grid(row = 5, column = 1)
        
    def go_add(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def go_edit(self):
        '''Screen.current = 2
        Screen.switch_frame()'''
        pop_up = tk.Tk()
        pop_up.title("Edit Selection")       
        frm_edit_entry = EditEntry(pop_up)
        frm_edit_entry.grid(row= 0, column = 0)
        
    def go_search(self):
        Screen.current = 3
        Screen.switch_frame()
        
    def go_remove(self):
        Screen.current = 4
        Screen.switch_frame()
        
    def go_save(self):
        Screen.current = 5
        Screen.switch_frame()
        
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
              
  
class Search(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text ="Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        options=["Genre", "Title", "Developer", "Publisher", "System",
                 "Release Date", "Rating","Game Mode", "Beat the Game",
                 "Purchase Date", "Price", "Notes"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 1, column = 0, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text ="Search For?", font = BUTTON_FONT)
        self.lbl_search_for.grid(row = 3, column = 0, sticky = "news")
        
        self.ent_box2 = tk.Entry(self)
        self.ent_box2.grid(row = 4, column = 0, sticky = "news")
        
        self.sct_box1 = ScrolledText(self, height = 8, width = 40)
        self.sct_box1.grid(row = 5, columnspan = 3, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "BACK", font = BUTTON_FONT)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", font = BUTTON_FONT)
        self.btn_clear.grid(row = 6, column = 1, sticky = "news")
        
        self.btn_submit = tk.Button(self, text = "SUBMIT", font = BUTTON_FONT)
        self.btn_submit.grid(row = 6, column = 2, sticky = "news")
        
        checkbox_filter = CheckboxFilter(self)
        checkbox_filter.grid(row = 2, column = 1, rowspan = 3, columnspan = 2, sticky = "news")
        
        
        
class Add(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text ="Add", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_genre = tk.Label(self, text="Genre?", font = BUTTON_FONT)
        self.lbl_genre.grid(row = 1, column =  0, sticky = "news")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.lbl_dev = tk.Label(self, text="Developer?", font = BUTTON_FONT)
        self.lbl_dev.grid(row = 2, column = 0 , sticky = "news")
        
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 2, column = 1, sticky = "news")
        
        self.lbl_title = tk.Label(self, text="Title?", font = BUTTON_FONT)
        self.lbl_title.grid(row = 1, column = 2 , sticky = "news")
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 1, column = 3, sticky = "news")
        
        self.lbl_pub = tk.Label(self, text="Publisher?", font = BUTTON_FONT)
        self.lbl_pub.grid(row = 2, column = 2, sticky = "news")
        
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 2, column = 3, sticky = "news")
        
        self.lbl_year = tk.Label(self, text="Year?", font = BUTTON_FONT)
        self.lbl_year.grid(row = 3, column = 0, sticky = "news")
        
        self.ent_year = tk.Entry(self)
        self.ent_year.grid(row = 3, column = 1, sticky = "news")
        
        self.lbl_beat = tk.Label(self, text="Beat It?", font = BUTTON_FONT)
        self.lbl_beat.grid(row = 4, column = 0, sticky = "news")
        
        self.ent_beat = tk.Entry(self)
        self.ent_beat.grid(row = 4, column = 1, sticky = "news")
        
        self.lbl_mode = tk.Label(self, text="Mode?", font = BUTTON_FONT)
        self.lbl_mode.grid(row = 4, column = 2, sticky = "news")
        
        options=["Single Player", "Multi-Player"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes?", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 5, column = 0, sticky = "news")
        
        self.sct_notes = ScrolledText(self, height = 8, width = 40)
        self.sct_notes.grid(row = 6, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 7, column = 0, sticky = "news")
        
        self.btn_reset = tk.Button(self, text ="Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 7, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text ="Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 7, column = 2, sticky = "news")
        
class Edit(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text ="Edit", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_genre = tk.Label(self, text="Genre?", font = BUTTON_FONT)
        self.lbl_genre.grid(row = 1, column =  0, sticky = "news")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.lbl_dev = tk.Label(self, text="Developer?", font = BUTTON_FONT)
        self.lbl_dev.grid(row = 2, column = 0 , sticky = "news")
        
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 2, column = 1, sticky = "news")
        
        self.lbl_title = tk.Label(self, text="Title?", font = BUTTON_FONT)
        self.lbl_title.grid(row = 1, column = 2 , sticky = "news")
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 1, column = 3, sticky = "news")
        
        self.lbl_pub = tk.Label(self, text="Publisher?", font = BUTTON_FONT)
        self.lbl_pub.grid(row = 2, column = 2, sticky = "news")
        
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 2, column = 3, sticky = "news")
        
        self.lbl_year = tk.Label(self, text="Year?", font = BUTTON_FONT)
        self.lbl_year.grid(row = 3, column = 0, sticky = "news")
        
        self.ent_year = tk.Entry(self)
        self.ent_year.grid(row = 3, column = 1, sticky = "news")
        
        self.lbl_beat = tk.Label(self, text="Beat It?", font = BUTTON_FONT)
        self.lbl_beat.grid(row = 4, column = 0, sticky = "news")
        
        self.ent_beat = tk.Entry(self)
        self.ent_beat.grid(row = 4, column = 1, sticky = "news")
        
        self.lbl_mode = tk.Label(self, text="Mode?", font = BUTTON_FONT)
        self.lbl_mode.grid(row = 4, column = 2, sticky = "news")
        
        options=["Single Player", "Multi-Player"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes?", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 5, column = 0, sticky = "news")
        
        self.sct_notes = ScrolledText(self, height = 8, width = 40)
        self.sct_notes.grid(row = 6, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 7, column = 0, sticky = "news")
        
        self.btn_reset = tk.Button(self, text ="Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 7, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text ="Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 7, column = 2, sticky = "news")        

class EditEntry(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.lbl_edit_title = tk.Label(self, text= "Which Title would you like to edit", font = BUTTON_FONT)
        self.lbl_edit_title.grid(row = 0, column = 0 , sticky = "news")
        
        options=["To Be Entered"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_ok = tk.Button(self, text ="Correct", font = BUTTON_FONT)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")

class Save(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_save = tk.Label(self, text="File Save!", font = BUTTON_FONT)
        self.lbl_save.grid(row = 0, column = 0 , sticky = "news")
        
        self.btn_ok = tk.Button(self, text ="Ok!", font = BUTTON_FONT)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")
        
class Remove(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_remove = tk.Label(self, text="Which Title would you like to remove?", font = BUTTON_FONT)
        self.lbl_remove.grid(row = 0, column = 0 , sticky = "news")
        
        options=["To Be Entered"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_ok = tk.Button(self, text ="Correct", font = BUTTON_FONT)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")      

class Rconfirm(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_rconfirm = tk.Label(self, text="These Games are Marked for Removal", font = BUTTON_FONT)
        self.lbl_rconfirm.grid(row = 0, column = 0 , sticky = "news")
        
        self.sct_rconfirm = ScrolledText(self, height = 8, width = 40)
        self.sct_rconfirm.grid(row = 1, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_verify = tk.Button(self, text ="Verify!", font = BUTTON_FONT)
        self.btn_verify.grid(row = 3, column = 0, sticky = "news")       



    
    


class CheckboxFilter(tk.Frame):
    def __init__(self, parent ):
        tk.Frame.__init__(self, master= parent)


        self.chk_title = tk.Checkbutton(self, text = "Title")
        self.chk_title.grid(row = 0, column = 0, sticky = "news")

        self.chk_genre = tk.Checkbutton(self, text = "Genre")
        self.chk_genre.grid(row = 1, column = 0, sticky = "news")

        self.chk_dev = tk.Checkbutton(self, text = "Developer")
        self.chk_dev.grid(row = 2, column = 0, sticky = "news")

        self.chk_pub = tk.Checkbutton(self, text = "Publisher")
        self.chk_pub.grid(row = 3, column = 0, sticky = "news")

        self.chk_platform = tk.Checkbutton(self,text = "Platform")
        self.chk_platform.grid(row = 0, column = 1, sticky = "news")

        self.chk_date = tk.Checkbutton(self, text = "Release Date")
        self.chk_date.grid(row = 1, column = 1, sticky = "news")

        self.chk_rate = tk.Checkbutton(self, text = "Rating")
        self.chk_rate.grid(row = 2, column = 1, sticky = "news" )

        self.chk_multi = tk.Checkbutton(self, text = "Single/Multi")
        self.chk_multi.grid(row = 3, column = 1, sticky = "news")

        self.chk_price = tk.Checkbutton(self, text = "Price")
        self.chk_price.grid(row = 0, column = 2, sticky = "news")

        self.chk_beat = tk.Checkbutton(self, text = "Beaten")
        self.chk_beat.grid(row = 1, column = 2, sticky = "news")        

        self.chk_beat = tk.Checkbutton(self, text = "Purchase Date")
        self.chk_beat.grid(row = 2, column = 2, sticky = "news")            

        self.chk_note = tk.Checkbutton(self, text = "Notes")
        self.chk_note.grid(row = 3, column = 2, sticky = "news") 
        
    
        
                      
##MAIN
if __name__ == "__main__":
    datafile = open("game_lib.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("500x500")
    root.grid_columnconfigure(0, weight = 1)
    screens = [MainMenu(),Add(),Edit(),Search(), Remove(), Save()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news")
    screens[0].tkraise()    
    
    root.mainloop()
    
    
