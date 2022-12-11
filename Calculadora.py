from tkinter import *
from tkinter import ttk, StringVar

cor1 = "#9dbfa3"
cor2 = "#0d0c0c"
cor3 = "#c2732f"


janela =Tk()
janela.title("calculadora")
janela.geometry("236x300")
janela.config(bg = cor2)

frame_tela = Frame(janela, width=236, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

#

todos_valores = ""
valor_texto = StringVar()

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",justify=RIGHT, font=('Ivy 17 bold'),bg=cor1)
app_label.place(x=0,y=0)


#botões

b_1 = Button(frame_corpo,command= limpar_tela, text= "C", width=13, height=2, bg=cor3, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=2, y=2)

b_2 = Button(frame_corpo,command= lambda :entrar_valores("%"),text="%", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=2)

b_3 = Button(frame_corpo,command= lambda :entrar_valores("/"), text= "/", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=2)
#linha2
b_4 = Button(frame_corpo,command= lambda :entrar_valores("7"),text= "7", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=1, y=50)

b_5 = Button(frame_corpo,command= lambda :entrar_valores("8"), text= "8", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=50)

b_6 = Button(frame_corpo,command= lambda :entrar_valores("9"), text= "9", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=50)

b_7 = Button(frame_corpo,command= lambda :entrar_valores("*"), text= "*", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=50)
#linha3
b_8 = Button(frame_corpo,command= lambda :entrar_valores("4"), text= "4", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=1, y=100)

b_9 = Button(frame_corpo,command= lambda :entrar_valores("5"), text= "5", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=100)

b_10 = Button(frame_corpo,command= lambda :entrar_valores("6"), text= "6", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=100)
#linha4
b_11 = Button(frame_corpo,command= lambda :entrar_valores("-"), text= "-", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=100)

b_12 = Button(frame_corpo,command= lambda :entrar_valores("1"), text= "1", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=1, y=150)

b_13 = Button(frame_corpo,command= lambda :entrar_valores("2"), text= "2", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=150)

b_14 = Button(frame_corpo,command= lambda :entrar_valores("3"), text= "3", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=150)

b_15 = Button(frame_corpo,command= lambda :entrar_valores("+"), text= "+", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=150)
#linha5
b_16 = Button(frame_corpo,command= lambda :entrar_valores("0"), text= "0", width=13, height=2, bg=cor3, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=2, y=200)

b_17 = Button(frame_corpo,command= lambda :entrar_valores("."), text= ".", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=200)

b_18 = Button(frame_corpo,command= calcular, text= "=", width=6, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=200)




janela.mainloop()
