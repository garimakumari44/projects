import tkinter as tk 
from tkinter import *
import re 





responses = {
    "hello" : ['hello, how can I help you? '], 
    "nausea" : ['you might be having fever ', 'how long have you being feeling this ?'], 
    "nausea and headache" : ["these can  can be symptoms of stomach flu", "how long you have been this ?"], 
    "numbness and loss of sensations" : ["this is a situation of puns and needles "],
    "runny noise, cough and diarrhea" : ["it might be that you are having common cold.", "what makes you think {} me?"], 
    "bloating and stomachache" : ['this cane be symptoms of gallstone' ], 
    "sorry" : ['there is no need to apologize', 'what are you apologizing for? '],
    "gas and constipation" : [' these common symptoms of Gastroesophageal reflux disease, or GERD.'], 
    'no symptoms' : ['why not?', 'oo okay but you elaborate?'],
    "severe" : ['Please visit our clinic']
    
}

root = tk.Tk()
root.geometry("500x570+100+30")
root.title(" HEALTHIFY")
root.resizable(0, 0)
#text = tk.StringVar()

centerFrame = tk.Frame(root)
centerFrame.place(x=100, y=50, height=350, width=350)

scrollbar = tk.Scrollbar(root)
scrollbar.place(x=450, y=50, height=350, width=20)

box_display = tk.Text(root, width=40, height=8, background="#F3CAF5",yscrollcommand=scrollbar.set)
box_display.place(x=100, y=50, height=350, width=350)
scrollbar.config(command=box_display.yview)

txt_input = tk.Entry(root, width=15)

def textReply():
    question = entry.get()
    box_display.insert( END, f"YOU: {question} \n ")
    entry.delete(0, END )
    
    response = get_response(question)
    box_display.insert(tk.END, f"Bot:  {response} \n")
    
    
def get_response( message):
        for pattern, response in responses.items():
            if re.match(pattern, message, re.IGNORECASE):
                
                return response
        return "I'm sorry, I didn't understand that."

label = tk.Label(root, text='welcome to healthify', height=30, width=50, justify=tk.LEFT, anchor='nw', font= {"family": "Arial Black", 'size': 20})
label.place(x=100, y=10, height=35, width=300)

entry = tk.Entry(root,width=72)
entry.place(x=100, y=450, height=50, width=350)













    









   
txt_input.delete(0, 'end')

button = tk.Button(root, text='Send', command=textReply)
button.place(x=150,y=500,height=40, width=150)


root.configure(bg="#8DE5AA")
box_display.configure(background='white')

root.mainloop()
