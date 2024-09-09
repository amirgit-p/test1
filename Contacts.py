from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database('d:/Contacts Manager.db')

def populate_list():   # ساکن کردن
    contact_list.delete(0, END)
    records = db.fetch()
    for row in records:
        contact_list.insert(END, f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}')
   
def add_item():
    if name_entry.get() == '' or family_entry.get() == '' or address_entry.get() == '' or phone_entry.get() == '':
        messagebox.showerror("خطا", "لطفا همه ي ورودي ها را پر کنيد")
        return
    db.insert(name_entry.get(), family_entry.get(),
              address_entry.get(), phone_entry.get())
    
    # contact_list.delete(0, END)
    # contact_list.insert(END, (name_text.get(), family_text.get(), address_text.get() , phone_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global record
        index = contact_list.curselection() #[0]
        selected_item = contact_list.get(index)
        print(selected_item)
        print(type(selected_item))
        record = selected_item.split(',')
        print(record)   
        clear_text()    
        name_entry.insert(END, record[1])
        family_entry.insert(END, record[2])        
        address_entry.insert(END, record[3])
        phone_entry.insert(END, record[4])
    except IndexError:
        pass

def remove_item():
    db.remove(record[0])
    clear_text()
    populate_list()

def update_item():
    global record
    db.update(record[0], name_entry.get(), family_entry.get(),
              address_entry.get(), phone_entry.get())
    populate_list()

def clear_text():
    name_entry.delete(0, END)
    family_entry.delete(0, END)
    address_entry.delete(0, END)
    phone_entry.delete(0, END)

def search_item():
    records = db.search(search_entry.get())
    contact_list.delete(0, END)
    for rec in records:
      contact_list.insert(END,rec)

win = Tk()

#Name
name_text = StringVar()
name_text = 'ali'
name_label = Label(win, text = "نام", font = ('Tahoma 14'), padx = 50, pady = 20)
name_label.grid(row = 0, column = 0)
name_entry = Entry(win, textvariable = name_text, bd = 3, relief = GROOVE)
name_entry.grid(row = 0, column = 1)

#Family
family_text = StringVar()
family_label = Label(win, text = "نام خانوادگي", font = ('Tahoma', 14), padx = 50, pady = 20)
family_label.grid(row = 0, column = 2)
family_entry = Entry(win, textvariable = family_text, bd = 3, relief = GROOVE)
family_entry.grid(row = 0, column = 3)

#Address
address_text = StringVar()
address_label = Label(win, text = "آدرس", font = ('Tahoma', 14), padx = 50, pady = 20)
address_label.grid(row = 1, column = 0)
address_entry = Entry(win, textvariable = address_text, bd = 3, relief = GROOVE)
address_entry.grid(row = 1, column = 1)

#Phone
phone_text = StringVar()
phone_label = Label(win, text = "شماره تلفن", font = ('Tahoma', 14), padx = 50, pady = 20)
phone_label.grid(row = 1, column = 2)
phone_entry = Entry(win, textvariable = phone_text, bd = 3, relief = GROOVE)
phone_entry.grid(row = 1, column = 3)

#Contacts List
contact_list = Listbox(win, height = 9, width = 100 ,bd = 3)    
contact_list.grid(row = 4, column = 0, columnspan = 3, rowspan = 6, pady = 20, padx = 20)

#Binding ListBox      widget.bind(event, handler)
contact_list.bind('<<ListboxSelect>>', select_item)

#Create Scrollbar
scrollbar = Scrollbar(win)
scrollbar.grid(row = 4, column = 3)

#Set Scroll To Listbox
contact_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = contact_list.yview)

#Buttons
add_btn = ttk.Button(win, text = "اضافه کردن", width = 18, command = add_item)
add_btn.grid(row = 2, column = 0, pady = 20)

remove_btn = ttk.Button(win, text = "حذف کردن", width = 18, command = remove_item)
remove_btn.grid(row = 2, column = 1)

update_btn = ttk.Button(win, text = "بروزرساني", width = 18, command = update_item)
update_btn.grid(row = 2, column = 2)

clear_btn = ttk.Button(win, text = "پاک کردن ورودي ها", width = 18, command = clear_text)
clear_btn.grid(row = 2, column = 3)

show_btn = ttk.Button(win, text = "نمایش لیست", width = 18, command = populate_list)
show_btn.grid(row = 3, column = 0)

search_btn = ttk.Button(win, text = "جستجو", width = 18, command = search_item)
search_btn.grid(row = 3, column = 1  )

search_text = StringVar()
search_entry = Entry(win, textvariable = search_text, bd = 3, relief = GROOVE)
search_entry.grid(row = 3, column = 2)

win.title("مديريت مخاطبين")
win.geometry('800x500')
win.resizable(0, 0)

win.mainloop()
