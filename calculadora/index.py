from tkinter import *
from tkinter import ttk

cor1 = "#363636"
cor2 = "#feff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela =Tk()
janela.title("calculator")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

janela.mainloop()  