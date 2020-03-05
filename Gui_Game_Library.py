#!usr/bin/python3
#Austin Andrews
#02/10/2020

'''Gui Version of the game library app'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

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
        screens[Screen.current].clear()
        Screen.switch_frame()
        
    def go_edit(self):
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
        
        self.btn_back = tk.Button(self, text = "BACK", font = BUTTON_FONT, command = self.go_main)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", font = BUTTON_FONT, command = self.clear)
        self.btn_clear.grid(row = 6, column = 1, sticky = "news")
        
        self.btn_submit = tk.Button(self, text = "SUBMIT", font = BUTTON_FONT, command = self.sumbit_search)
        self.btn_submit.grid(row = 6, column = 2, sticky = "news")
        
        self.checkbox_filter = CheckboxFilter(self)
        self.checkbox_filter.grid(row = 2, column = 1, rowspan = 3, columnspan = 2, sticky = "news")
        
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def filter_print(self, entry):
        if self.checkbox_filter.title_filter.get() == True:     
            msg = entry[0]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.genre_filter.get() == True:     
            msg = entry[1]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.dev_filter.get() == True:     
            msg = entry[2]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.pub_filter.get() == True:     
            msg = entry[3]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.platform_filter.get() == True:     
            msg = entry[4]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.date_filter.get() == True:     
            msg = entry[5]+"\n"
            self.sct_box1.insert("insert", msg) 
        
        if self.checkbox_filter.rate_filter.get() == True:     
            msg = entry[6]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.beat_filter.get() == True:     
            msg = entry[7]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.purch_filter.get() == True:     
            msg = entry[8]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.multi_filter.get() == True:     
            msg = entry[9]+"\n"
            self.sct_box1.insert("insert", msg)
            
        if self.checkbox_filter.price_filter.get() == True:     
            msg = entry[10]+"\n"
            self.sct_box1.insert("insert", msg)        
            
        if self.checkbox_filter.note_filter.get() == True:     
            msg = entry[11]+"\n"
            self.sct_box1.insert("insert", msg)        
            
            
        msg = "************\n"
        self.sct_box1.insert("insert", msg)
        
        
    def clear(self):
        self.checkbox_filter.title_filter.set(False)
        self.checkbox_filter.genre_filter.set(False)
        self.checkbox_filter.dev_filter.set(False)
        self.checkbox_filter.pub_filter.set(False)
        self.checkbox_filter.platform_filter.set(False)
        self.checkbox_filter.date_filter.set(False)
        self.checkbox_filter.rate_filter.set(False)
        self.checkbox_filter.beat_filter.set(False)
        self.checkbox_filter.price_filter.set(False)
        self.checkbox_filter.purch_filter.set(False)
        self.checkbox_filter.multi_filter.set(False)
        self.checkbox_filter.note_filter.set(False)
        
        
        self.sct_box1.delete(0.0, "end")
        
        
    def sumbit_search(self):
        self.sct_box1.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
            
    def [r
        
        
        
class Add(Screen):
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
        
        self.lbl_platform = tk.Label(self, text="Platform?", font = BUTTON_FONT)
        self.lbl_platform.grid(row = 3, column = 2, sticky = "news")
        
        self.ent_platform = tk.Entry(self)
        self.ent_platform.grid(row = 3, column = 3, sticky = "news")        
        
        self.lbl_year = tk.Label(self, text="Year?", font = BUTTON_FONT)
        self.lbl_year.grid(row = 3, column = 0, sticky = "news")
        
        self.ent_year = tk.Entry(self)
        self.ent_year.grid(row = 3, column = 1, sticky = "news")
        
        self.lbl_rating = tk.Label(self, text="Rating?", font = BUTTON_FONT)
        self.lbl_rating.grid(row = 5, column = 0, sticky = "news")
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row = 5, column = 1, sticky = "news")        
        
        self.lbl_beat = tk.Label(self, text="Beat It?", font = BUTTON_FONT)
        self.lbl_beat.grid(row = 4, column = 0, sticky = "news")
        
        self.ent_beat = tk.Entry(self)
        self.ent_beat.grid(row = 4, column = 1, sticky = "news")
        
        
        self.lbl_purch = tk.Label(self, text="Purch. Date?", font = BUTTON_FONT)
        self.lbl_purch.grid(row = 5, column = 2, sticky = "news")
        
        self.ent_purch = tk.Entry(self)
        self.ent_purch.grid(row = 5, column = 3, sticky = "news")        
        
        
        
        self.lbl_mode = tk.Label(self, text="Mode?", font = BUTTON_FONT)
        self.lbl_mode.grid(row = 4, column = 2, sticky = "news")
        
        options=["Single Player", "Multi-Player"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes?", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 6, column = 0, sticky = "news")
        
        self.sct_notes = ScrolledText(self, height = 8, width = 40)
        self.sct_notes.grid(row = 7, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.main)
        self.btn_cancel.grid(row = 8, column = 0)
        
        self.btn_reset = tk.Button(self, text ="Reset", font = BUTTON_FONT, command = self.clear)
        self.btn_reset.grid(row = 8, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text ="Confirm", font = BUTTON_FONT, command = self.go_main)
        self.btn_confirm.grid(row = 8, column = 2)        
        
    def go_main(self):
        Screen.current = 0
        messagebox.showinfo(message = "Entry Has been Added")        
        Screen.switch_frame()
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_title.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_platform.get())
        entry.append(self.ent_year.get())
        entry.append(self.ent_rating.get())
        entry.append(self.tkvar.get())
        entry.append(self.ent_beat.get())
        entry.append(self.ent_purch.get())
        entry.append(self.sct_notes.get(0.0, "end"))
        games[len(games) +1] = entry        
        
    def clear(self):
        self.ent_genre.delete(0, "end")
        self.ent_title.delete(0, "end")
        self.ent_dev.delete(0, "end")
        self.ent_pub.delete(0, "end")
        self.ent_platform.delete(0, "end")
        self.ent_year.delete(0, "end")
        self.ent_rating.delete(0, "end")
        self.ent_beat.delete(0, "end")
        self.ent_purch.delete(0, "end")  
        
        
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()        
        

class PopMessage(tk.Frame):
    def __init__(self, parent, msg = "Generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        
        self.lbl_continue = tk.Label(self, text = msg)
        self.lbl_continue.grid(row = 0, column = 0)
        
        self.btn_ok = tk.Button(self, text = "Ok", command = self.parent.destroy)
        self.btn_ok.grid(row = 1, column = 0)



        
        
class Edit(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
               
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
        
        self.lbl_platform = tk.Label(self, text="Platform?", font = BUTTON_FONT)
        self.lbl_platform.grid(row = 3, column = 2, sticky = "news")
        
        self.ent_platform = tk.Entry(self)
        self.ent_platform.grid(row = 3, column = 3, sticky = "news")        
        
        self.lbl_year = tk.Label(self, text="Year?", font = BUTTON_FONT)
        self.lbl_year.grid(row = 3, column = 0, sticky = "news")
        
        self.ent_year = tk.Entry(self)
        self.ent_year.grid(row = 3, column = 1, sticky = "news")
        
        self.lbl_rating = tk.Label(self, text="Rating?", font = BUTTON_FONT)
        self.lbl_rating.grid(row = 5, column = 0, sticky = "news")
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row = 5, column = 1, sticky = "news")        
        
        self.lbl_beat = tk.Label(self, text="Beat It?", font = BUTTON_FONT)
        self.lbl_beat.grid(row = 4, column = 0, sticky = "news")
        
        self.ent_beat = tk.Entry(self)
        self.ent_beat.grid(row = 4, column = 1, sticky = "news")
        
        
        self.lbl_purch = tk.Label(self, text="Purch. Date?", font = BUTTON_FONT)
        self.lbl_purch.grid(row = 5, column = 2, sticky = "news")
        
        self.ent_purch = tk.Entry(self)
        self.ent_purch.grid(row = 5, column = 3, sticky = "news")        
        
        
        
        self.lbl_mode = tk.Label(self, text="Mode?", font = BUTTON_FONT)
        self.lbl_mode.grid(row = 4, column = 2, sticky = "news")
        
        options=["Single Player", "Multi-Player"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *options)
        self.menu.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes?", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 6, column = 0, sticky = "news")
        
        self.sct_notes = ScrolledText(self, height = 8, width = 40)
        self.sct_notes.grid(row = 7, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.go_main)
        self.btn_cancel.grid(row = 8, column = 0)
        
        self.btn_reset = tk.Button(self, text ="Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 8, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text ="Confirm", font = BUTTON_FONT, command = self.go_main)
        self.btn_confirm.grid(row = 8, column = 2)
        
    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])

        self.ent_title.delete(0, "end")        
        self.ent_title.insert(0, entry[1])
                              
        self.ent_dev.delete(0, "end")                      
        self.ent_dev.insert(0, entry[2])
        
        self.ent_pub.delete(0, "end")
        self.ent_pub.insert(0, entry[3])
        

        self.ent_platform.delete(0, "end")        
        self.ent_platform.insert(0, entry[4])

        self.ent_year.delete(0, "end")        
        self.ent_year.insert(0, entry[5])

        self.ent_rating.delete(0, "end")        
        self.ent_rating.insert(0, entry[6])

        self.ent_beat.delete(0, "end")        
        self.ent_beat.insert(0, entry[8])

        self.ent_purch.delete(0, "end")        
        self.ent_purch.insert(0, entry[9])
        
        
    def go_main(self):
        self.confirm_edit()
        Screen.current = 0
        Screen.switch_frame() 
        
    def confirm_edit(self):
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_title.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_platform.get())
        entry.append(self.ent_year.get())
        entry.append(self.ent_rating.get())
        entry.append(self.tkvar.get())
        entry.append(self.ent_beat.get())
        entry.append(self.ent_purch.get())
        entry.append(self.sct_notes.get(0.0, "end"))
        games[self.edit_key] = entry
        
        

class EditEntry(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.lbl_edit_title = tk.Label(self, text= "Which Title would you like to edit", font = BUTTON_FONT)
        self.lbl_edit_title.grid(row = 0, column = 0 , sticky = "news")
        
        self.options=["Select A Title"]
        for key in games.keys():
            self.options.append(games[key][1])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.menu = tk.OptionMenu(self,
                                  self.tkvar, *self.options)
        self.menu.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.go_main)
        self.btn_cancel.grid(row = 2, column = 0)
        
        self.btn_confirm = tk.Button(self, text ="Confirm", font = BUTTON_FONT, command = self.go_edit)
        self.btn_confirm.grid(row = 3, column = 0)  
        
    def go_main(self):
        self.parent.destroy()
        Screen.current = 0
        Screen.switch_frame()
        
    def go_edit(self):  
        if self.tkvar.get() == self.options[0]:
            popup = tk.Tk()
            popup.title("Edit")
            msg ="Error, select a title"
            frm_error = PopMessage(popup, msg)
            frm_error.grid(row = 0, column = 0)
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[2].edit_key = i
                    break
            Screen.current = 2
            screens[Screen.current].update()
            Screen.switch_frame()
            self.parent.destroy()
        
        
class Save(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_save = tk.Label(self, text="File Save!", font = BUTTON_FONT)
        self.lbl_save.grid(row = 0, column = 0 , sticky = "news")
        
        self.btn_ok = tk.Button(self, text ="Ok!", font = BUTTON_FONT, command = self.go_main)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame() 
        
    
        
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
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.go_main)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_ok = tk.Button(self, text ="Correct", font = BUTTON_FONT, command = self.go_remove)
        self.btn_ok.grid(row = 3, column = 0, sticky = "news")
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def go_remove(self):
        Screen.current = 4
        Screen.switch_frame()     

class Rconfirm(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_rconfirm = tk.Label(self, text="These Games are Marked for Removal", font = BUTTON_FONT)
        self.lbl_rconfirm.grid(row = 0, column = 0 , sticky = "news")
        
        self.sct_rconfirm = ScrolledText(self, height = 8, width = 40)
        self.sct_rconfirm.grid(row = 1, columnspan = 3, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.go_main)
        self.btn_cancel.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_verify = tk.Button(self, text ="Verify!", font = BUTTON_FONT)
        self.btn_verify.grid(row = 3, column = 0, sticky = "news")
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()   



    
    


class CheckboxFilter(tk.Frame):
    def __init__(self, parent ):
        tk.Frame.__init__(self, master= parent)

        self.title_filter = tk.BooleanVar()
        self.title_filter.set(True)
        self.chk_title = tk.Checkbutton(self, text = "Title", variable = self.title_filter)
        self.chk_title.grid(row = 0, column = 0, sticky = "news")

        self.genre_filter = tk.BooleanVar()
        self.genre_filter.set(True)        
        self.chk_genre = tk.Checkbutton(self, text = "Genre", variable = self.genre_filter)
        self.chk_genre.grid(row = 1, column = 0, sticky = "news")

        self.dev_filter = tk.BooleanVar()
        self.dev_filter.set(True)        
        self.chk_dev = tk.Checkbutton(self, text = "Developer", variable = self.dev_filter)
        self.chk_dev.grid(row = 2, column = 0, sticky = "news")
        
        self.pub_filter = tk.BooleanVar()
        self.pub_filter.set(True)        
        self.chk_pub = tk.Checkbutton(self, text = "Publisher", variable = self.pub_filter)
        self.chk_pub.grid(row = 3, column = 0, sticky = "news")

        self.platform_filter = tk.BooleanVar()
        self.platform_filter.set(True)
        self.chk_platform = tk.Checkbutton(self,text = "Platform", variable = self.platform_filter)
        self.chk_platform.grid(row = 0, column = 1, sticky = "news")

        self.date_filter = tk.BooleanVar()
        self.date_filter.set(True)        
        self.chk_date = tk.Checkbutton(self, text = "Release Date", variable = self.date_filter)
        self.chk_date.grid(row = 1, column = 1, sticky = "news")

        self.rate_filter = tk.BooleanVar()
        self.rate_filter.set(True)        
        self.chk_rate = tk.Checkbutton(self, text = "Rating", variable = self.rate_filter)
        self.chk_rate.grid(row = 2, column = 1, sticky = "news" )

        self.multi_filter = tk.BooleanVar()
        self.multi_filter.set(True)
        self.chk_multi = tk.Checkbutton(self, text = "Single/Multi", variable = self.multi_filter)
        self.chk_multi.grid(row = 3, column = 1, sticky = "news")

        self.price_filter = tk.BooleanVar()
        self.price_filter.set(True)        
        self.chk_price = tk.Checkbutton(self, text = "Price", variable = self.price_filter)
        self.chk_price.grid(row = 0, column = 2, sticky = "news")

        self.beat_filter = tk.BooleanVar()
        self.beat_filter.set(True)        
        self.chk_beat = tk.Checkbutton(self, text = "Beaten", variable = self.beat_filter)
        self.chk_beat.grid(row = 1, column = 2, sticky = "news")        

        self.purch_filter = tk.BooleanVar()
        self.purch_filter.set(True)        
        self.chk_purch = tk.Checkbutton(self, text = "Purchase Date", variable = self.purch_filter)
        self.chk_purch.grid(row = 2, column = 2, sticky = "news")            

        self.note_filter = tk.BooleanVar()
        self.note_filter.set(True)
        self.chk_note = tk.Checkbutton(self, text = "Notes", variable = self.note_filter)
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