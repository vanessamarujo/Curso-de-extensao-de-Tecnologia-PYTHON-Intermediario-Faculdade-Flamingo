
#importando a biblioteca tkinter
from tkinter import*

#criando a janelade nome Top
top=Tk()
#definindo o tamanho da janela(largura x altura)
top.geometry("200x100")
#criação e definição de um botão
b=Button(top,text="Simple")
#inserção do botão na janela criada no tkinter
b.pack()
#chamada para criação da função
top.mainloop()