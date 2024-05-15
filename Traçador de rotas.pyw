# Tracert é um comando do CMD (Prompt de comandos do Windows) que serve
#	para traçar a rota do seu computador até o IP ou site desejado

# Para ver como funciona, digite um IP ou URL de site e aperte o botão "Traçar rota"
# IMPORTANTE: Isso pode demorar um minuto ou mais porque o tracert traça a rota em até 30 níveis

from tkinter import *
import os, re, subprocess
from tkinter import messagebox

app = Tk()
app.title("Traçador de rotas")
app.resizable(False, False)
app.geometry("545x290+600+300")
app.config(bg=None)

comando = StringVar()

def tracert():
    global comando
    cmd = "tracert " + str(comando.get())
    resultado = "".join(os.popen(cmd).readlines())
    tx1.insert(END, resultado)

lb1 = Label(app, text="IP ou URL").place(x=5, y=5)
et1 = Entry(app, width=60, textvariable=comando).place(x=65, y=5)
bt1 = Button(app, text="Traçar rota", width=10, bd=3, command=tracert).place(x=435, y=2)
tx1 = Text(app, bd=2, width=66, height=15)
tx1.place(x=5, y=35)

app.mainloop()