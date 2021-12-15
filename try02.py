import tkinter as tk

def setู_message():
    text=text_input.get()
    title_lable.configure(text=text)

window=tk.Tk()
window.title('justPython')
window.minsize(width=400,height=400)

title_lable=tk.Label(master=window,text='krit eiei')
title_lable.pack()

text_input=tk.Entry(master=window)
text_input.pack()

ok_button=tk.Button(master=window,text='ได้แก่', command=set_message)
ok_button.pack()

window.mainloop()