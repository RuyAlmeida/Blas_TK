import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title('BLAS_tk')
root.geometry("1920x1080")

def raise_frame(Frames):
    Frames.tkraise()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

for Frame in (f1, f2, f3, f4, f5):
    Frame.grid(row=7, column=0)

#Botões do frame1
Button = ttk.Button(f1, text='Início',command=lambda:raise_frame(f1))
Button.grid(row=0, column=0, padx=20, pady=20)

Button = ttk.Button(f1, text='Financeiro',command=lambda:raise_frame(f2))
Button.grid(row=1, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f1, text='Transporte',command=lambda:raise_frame(f3))
Button.grid(row=2, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f1, text='Saúde',command=lambda:raise_frame(f4))
Button.grid(row=3, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f1, text='Rotina',command=lambda:raise_frame(f5))
Button.grid(row=4, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f1, text='Finalizar',command=root.destroy)
Button.grid(row=5, column=0, sticky='s', ipadx=20, ipady=20)

#Botões do frame2
Button = ttk.Button(f2, text='Início',command=lambda:raise_frame(f1))
Button.grid(row=0, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f2, text='Financeiro',command=lambda:raise_frame(f2))
Button.grid(row=1, column=0, padx=20, pady=20)

Button = ttk.Button(f2, text='Transporte',command=lambda:raise_frame(f3))
Button.grid(row=2, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f2, text='Saúde',command=lambda:raise_frame(f4))
Button.grid(row=3, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f2, text='Rotina',command=lambda:raise_frame(f5))
Button.grid(row=4, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f2, text='Finalizar',command=root.destroy)
Button.grid(row=5, column=0, ipadx=20, ipady=20)

#Botões do frame3
Button = ttk.Button(f3, text='Início',command=lambda:raise_frame(f1))
Button.grid(row=0, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f3, text='Financeiro',command=lambda:raise_frame(f2))
Button.grid(row=1, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f3, text='Transporte',command=lambda:raise_frame(f3))
Button.grid(row=2, column=0, padx=20, pady=20)

Button = ttk.Button(f3, text='Saúde',command=lambda:raise_frame(f4))
Button.grid(row=3, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f3, text='Rotina',command=lambda:raise_frame(f5))
Button.grid(row=4, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f3, text='Finalizar',command=root.destroy)
Button.grid(row=5, column=0, ipadx=20, ipady=20)

#Botões do frame4
Button = ttk.Button(f4, text='Início',command=lambda:raise_frame(f1))
Button.grid(row=0, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f4, text='Financeiro',command=lambda:raise_frame(f2))
Button.grid(row=1, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f4, text='Transporte',command=lambda:raise_frame(f3))
Button.grid(row=2, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f4, text='Saúde',command=lambda:raise_frame(f4))
Button.grid(row=3, column=0, padx=20, pady=20)

Button = ttk.Button(f4, text='Rotina',command=lambda:raise_frame(f5))
Button.grid(row=4, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f4, text='Finalizar',command=root.destroy)
Button.grid(row=5, column=0, ipadx=20, ipady=20)

#Botões do frame5
Button = ttk.Button(f5, text='Início',command=lambda:raise_frame(f1))
Button.grid(row=0, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f5, text='Financeiro',command=lambda:raise_frame(f2))
Button.grid(row=1, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f5, text='Transporte',command=lambda:raise_frame(f3))
Button.grid(row=2, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f5, text='Saúde',command=lambda:raise_frame(f4))
Button.grid(row=3, column=0, ipadx=20, ipady=20)

Button = ttk.Button(f5, text='Rotina',command=lambda:raise_frame(f5))
Button.grid(row=4, column=0, padx=20, pady=20)

Button = ttk.Button(f5, text='Finalizar',command=root.destroy)
Button.grid(row=5, column=0, ipadx=20, ipady=20)

#teste frame de aplicações
frame = tk.Frame(f1, width=1805, height=1080)
frame.place(anchor='e')

test_button = ttk.Button(f1, text='Transporte',command=root.destroy)
test_button.place(x=117, y=0, width=1805, height=1080)

#test_button = ttk.Button(frame, text='Saúde',command=root.destroy)
#test_button.place(x=0, y=300, width=100, height=100)

#test_button = ttk.Button(frame, text='Rotina',command=root.destroy)
#test_button.place(x=0, y=400, width=100, height=100)

#test_button = ttk.Button(frame, text='Fechar',command=root.destroy)
#test_button.place(x=0, y=950, width=100, height=100)

raise_frame(f1)
root.mainloop()