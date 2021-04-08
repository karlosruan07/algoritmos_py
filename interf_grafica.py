#Este programa mostra os fundamentos da biblioteca thinter;

from classe_hospital import *
from tkinter import *

hosp = hospital(nome='', tipo='', especialidade='', avaliacao='')

app = Tk()
app.geometry('300x300+200+100')
bt_inserir = Button(app, text='Inserir', command = hosp.inserir)
bt_inserir.pack()

bt_mostrar = Button(app, text='Mostrar', command = hosp.mostrar)
bt_mostrar.pack()
app.mainloop()