from tkinter import *
from PIL import ImageTk, Image
import random
#В зависимости от числа ставит картинку
def changePlayer():
    if var.get() == 0:
        panels.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
        panelk.grid_remove()
        panelp.grid_remove()
    elif var.get() == 1:
        panelk.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
        panels.grid_remove()
        panelp.grid_remove()
    elif var.get() == 2:
        panelp.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
        panelk.grid_remove()
        panels.grid_remove()
#В зависимости от числа ставит картинку для ПК и проверяет что стоит у игрока
def changePC():
    PK = random.randint(0, 2)
    Label1 = Label(root, text=" ")
    Label1.grid_remove()
    if PK == 0:
        PKpanels.grid(row=3, column=3000)
        PKpanelk.grid_remove()
        PKpanelp.grid_remove()
        if var.get() == 0:
            e = '  Ничья  '
            Label1 = Label(root, text=e)
        elif var.get() == 2:
            e = ' Выиграл '
            Label1 = Label(root, text=e)
        elif var.get() == 1:
            e = ' Проиграл '
            Label1 = Label(root, text=e)
    elif PK == 1:
        PKpanelk.grid(row=3, column=3000)
        PKpanels.grid_remove()
        PKpanelp.grid_remove()
        if var.get() == 1:
            e = ' Ничья '
            Label1 = Label(root, text=e)
        elif var.get() == 0:
            e = ' Выиграл '
            Label1 = Label(root, text=e)
        elif var.get() == 2:
            e = ' Проиграл '
            Label1 = Label(root, text=e)
    elif PK == 2:
        PKpanelp.grid(row=3, column=3000)
        PKpanelk.grid_remove()
        PKpanels.grid_remove()
        if var.get() == 2:
            e = ' Ничья '
            Label1 = Label(root, text=e)
        elif var.get() == 1:
            e = ' Выиграл '
            Label1 = Label(root, text=e)
        elif var.get() == 0:
            e = ' Проиграл '
            Label1 = Label(root, text=e)

    Label1.grid(row=5, column=0)
root = Tk()
root.geometry('1000x1000')
#Переменая из каторой с помощью .get можно считать информацию
var = IntVar()
var.set(0)
#Радиобатаны
Stone = Radiobutton(text="Stone", variable=var, value=0, command=changePlayer)
Knife = Radiobutton(text="Knife", variable=var, value=1, command=changePlayer)
Paper = Radiobutton(text="Paper", variable=var, value=2, command=changePlayer)
#Изобрадения
imgs = ImageTk.PhotoImage(Image.open("stone.png"))
imgk = ImageTk.PhotoImage(Image.open("knife.png"))
imgp = ImageTk.PhotoImage(Image.open("paper.png"))
#Панели с изображениями
panels = Label(root, image = imgs)
panelk = Label(root, image = imgk)
panelp = Label(root, image = imgp)
#Размещаем кнопки
Stone.grid(row=0, column=0)
Knife.grid(row=1, column=0)
Paper.grid(row=2, column=0)
#Чтобы сразу была картика камня по умолчанию
panels.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
panelk.grid_remove()
panelp.grid_remove()
#Панели с изображениями для ПК
PKpanels = Label(root, image = imgs)
PKpanelk = Label(root, image = imgk)
PKpanelp = Label(root, image = imgp)
#нопки чтобы играть
PKBut = Button(root,command=changePC,text='Играть').grid(row=4, column=0)


root.mainloop()