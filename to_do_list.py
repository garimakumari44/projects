import tkinter  as tk
from tkinter import *
import tkinter as ttk


tasks = []

def clear_listbox():
    for task in tasks:
        list_task.delete(0, "end")

def update_listbox():
    clear_listbox()
    for task in tasks:
        list_task.insert("end", task)
        

        
        

def add_task():
    task = txt_input.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else: 
        box_display['text'] = 'Please enter a task '
    txt_input.delete(0, 'end')
        
    

def delete_all():
    global tasks
    tasks = []
    update_listbox()
    
    
    
    
    

def delete_one():
    task = list_task.get(ANCHOR)
    if task in tasks:
        tasks.remove(task)
        
    update_listbox()

def exit():
    pass
    

root = tk.Tk()
root.title("GARIMA'S TO DO LIST")
root.geometry("400x650+400+100")
root.configure(bg="#CAE7F5")

root.resizable(False,False )
box_title = tk.Label(root, text="GARIMA'S TO DO LIST", width=24, background="#F3CAF5", font=( "Comic Sans MS",  20,  "bold") )
box_title.pack()
list_task = tk.Listbox(root, bg='#ECF5CA', height=25, width=40)
list_task.pack()


box_display = tk.Label(root, text="", background="#F3CAF5", font=("fraktur", 24) )
box_display.pack()
txt_input = tk.Entry(root, width=15)
txt_input.pack()


btn_add_task = tk.Button(root, text="Add Task", fg='green', bg='#F9DDE9', command=add_task)
btn_add_task.pack()

btn_delete_one = tk.Button(root, text="Delete", fg='green', bg='#A3DAEE', command=delete_one)
btn_delete_one.pack()






root.mainloop()