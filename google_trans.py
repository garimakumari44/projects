from tkinter import *
import tkinter as tk
from tkinter import ttk 
from googletrans import Translator, LANGUAGES

translator = Translator()

    

def translate_text(self):
        input_text = comb_sor.get()
        translated_text = translator.translate(input_text, dest='fr').text
        dest_txt.delete(1.0, tk.END)
        dest_txt.insert(tk.END, translated_text)
        
        

 

root = tk.Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='yellow')


label_text = Label(root, text='Translator', font=('Times New Roman', 40, 'bold'))
label_text.place(x=100, y=40, height=50, width=300)

frame = ttk.Frame(root).pack(side=BOTTOM)
Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=30, y=300, height=40, width=100)
comb_sor.set('english')


button_change = Button(frame, text='Translate', relief=RAISED, command=translate_text)
button_change.place(x=170,y=300,height=40, width=150)





comb_dest = ttk.Combobox( frame, value=list_text)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("english")




dest_txt = Text(frame, font=("Time New Roman", 20, 'bold'), wrap=WORD)
dest_txt.place(x=10, y=360, height=150, width=480)







root.mainloop()

