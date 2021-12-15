import tkinter as tk

def show_output():
    number=int(number_input.get())

    output=''
    for i in range(1,25):
        output+=str(number)+'x'+str(i)
        output+='='+ str(number*i)+'\n'

    output_labble.configure(text=output)

window=tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400,height=500)

title_lable=tk.Label(master=window,text='สูตรคูณแม่')
title_lable.pack()

number_input=tk.Entry(master=window)
number_input.pack()

go_button=tk.Button(
    master=window,text='ได้แก่',
    command=show_output
)
go_button.pack()

output_labble=tk.Label(master=window)
output_labble.pack(


window.mainloop()