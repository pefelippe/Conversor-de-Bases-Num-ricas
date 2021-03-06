from tkinter import *

# funções
def binario ():
    num= int(ed.get(), 2)
    lb4["text"] = 'Convertido para a base Octal: {}'.format(oct(num)[2:])
    lb5["text"] = 'Convertido para a base Decimal: {}'.format(int(num))
    lb6["text"] = 'Convertido para a base Hexadecimal: {}'.format(hex(num)[2:])
def octal ():
    num = int(ed.get(), 8)
    lb4["text"] = 'Convertido para a base Binaria: {}'.format(bin(num)[2:])
    lb5["text"] = 'Convertido para a base Decimal: {}'.format(int(num))
    lb6["text"] = 'Convertido para a base Hexadecimal: {}'.format(hex(num)[2:])
def decimal ():
    num = int(ed.get())
    lb4["text"] = 'Convertido para a base Binária: {}'.format(bin(num)[2:])
    lb5["text"] = 'Convertido para a base Octal: {}'.format(oct(num)[2:])
    lb6["text"] = 'Convertido para a base Hexadecimal: {}'.format(hex(num)[2:])
def hexadecimal():
    num = int(ed.get(), 16)
    lb4["text"] = 'Convertido para a base Binária: {}'.format(bin(num)[2:])
    lb5["text"] = 'Convertido para a base Octal: {}'.format(oct(num)[2:])
    lb6["text"] = 'Convertido para a base Decimal: {}'.format(int(num))

# configurações da janela
janela = Tk()
janela.geometry("585x380+400+200")
janela.title ("Conversor de Bases")


# labels
lb1= Label(janela, text="Digite seu número abaixo:")
lb1.place(x=180, y = 0) 
lb2= Label(janela, text="Informe a BASE ATUAL do seu número: ")
lb2.place(x=170, y=60)
lb3 = Label(janela, text="Resultado:")
lb3.place(x=30,y=220)
lb4 = Label(janela, text="Aguardando...")
lb4.place(x=30, y=250)
lb5 = Label(janela, text="")
lb5.place(x=30, y= 280)
lb6 = Label(janela, text = "")
lb6.place(x=30, y=310)
lb7 = Label (janela, text = "Obrigado por usar!")
lb7.place(x=450, y = 340)

# entrada de dados   
ed =  Entry (janela)
ed.place(x=205, y= 25)

# botões
bt1 = Button(janela, width=20, text = "Binária", command = binario)
bt1.place(x= 200, y=90)
bt2 = Button(janela, width = 20, text = "Octal", command = octal)
bt2.place(x=200, y=120)
bt3 = Button(janela, width = 20, text = "Decimal", command = decimal)
bt3.place(x=200, y =150)
bt4 = Button(janela, width =20, text = "Hexadecimal", command= hexadecimal)
bt4.place(x= 200, y=180)

janela.mainloop()

