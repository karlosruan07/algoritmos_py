#Este programa mostra como criar uma interface com um butão integrado.

from tkinter import *

from ola_mundo import *



app = Tk()
app.geometry('400x400+200+100')

x = olamundo()

butao_olamundo = Button(app, text='Olá, Mundo !', command = x.mostrar)
butao_olamundo.pack()

app.mainloop()