import tkinter as tk
import PIL as pl
import random
name=" "
vin=0
nich=0
los=0
class Demo1(tk.Tk):
    #Класс создания основного окна
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.Entry = tk.Entry(self, width=50, bg="white", fg="black", borderwidth=5)
        self.Entry.pack()
        self.Entry.insert(0, "Enter Your Name")
        self.button1 = tk.Button(self, text='Камень ножницы бумага', width=25, command=self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self, text='Информация', width=25, command=self.new_info_window)
        self.button2.pack()
        self.button3 = tk.Button(self, text = 'Записать имя', width = 25, command = self.Zapis)
        self.button3.pack()
    def Zapis(self):
        global name
        nam = self.Entry.get()
        name=nam
    def new_info_window(self):
        InfoWindow(self, "Программу создали Кондрашин Никита Андреевич и Япрынцев Тимур Алексеевич")

    def new_window(self):
        global name
        self.app = Demo2()
        self.app.title("Камень ножницы бумага "+ name)
        self.app.geometry('1000x1000')
        self.app.mainloop()

class InfoWindow():
    # Класс создания информационного окна
    def __init__(self, root, label):
        self.top = tk.Toplevel(root)
        self.top.geometry('500x50')
        self.label = tk.Label(self.top, text=label).pack()
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()

class Demo2(tk.Toplevel):
    # Класс создания нового окна
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        global name
        global vin
        global nich
        global los
        # Переменая из каторой с помощью .get можно считать информацию
        var = tk.IntVar()
        # Радиобатаны
        self.Stone = tk.Radiobutton(self,text="Stone", variable=var, value=0, command=lambda per=0: self.changePlayer(per)).grid(row=0, column=0)
        self.Knife = tk.Radiobutton(self,text="Knife", variable=var, value=1, command=lambda per=1: self.changePlayer(per)).grid(row=1, column=0)
        self.Paper = tk.Radiobutton(self,text="Paper", variable=var, value=2, command=lambda per=2: self.changePlayer(per)).grid(row=2, column=0)

        self.Konez = tk.Button(self, text="Закончить играть и сохранить результат",command= self.result).grid(row=6,column=0)

        # Изобрадения
        self.imgs = tk.PhotoImage(file="C:/Users/nikit\OneDrive\Рабочий стол\П4\stone.png")
        self.imgk = tk.PhotoImage(file="C:/Users/nikit\OneDrive\Рабочий стол\П4\knife.png")
        self.imgp = tk.PhotoImage(file="C:/Users/nikit\OneDrive\Рабочий стол\П4\paper.png")
        # Панели с изображениями
        self.panels = tk.Label(self, image=self.imgs)
        self.panelk = tk.Label(self, image=self.imgk)
        self.panelp = tk.Label(self, image=self.imgp)
        # Чтобы сразу была картика камня по умолчанию
        self.panels.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
        self.panelk.grid_remove()
        self.panelp.grid_remove()
        # Панели с изображениями для ПК
        PKpanels = tk.Label(self, image=self.imgs)
        PKpanelk = tk.Label(self, image=self.imgk)
        PKpanelp = tk.Label(self, image=self.imgp)
        self.PKpanels = tk.Label(self, image=self.imgs)
        self.PKpanelk = tk.Label(self, image=self.imgk)
        self.PKpanelp = tk.Label(self, image=self.imgp)
        PKBut = tk.Button(self, command=lambda : self.changePC(var.get()), text='Играть').grid(row=4, column=0)
    def changePlayer(self,per):
        if per == 0:
            self.panels.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
            self.panelk.grid_remove()
            self.panelp.grid_remove()
        elif per == 1:
            self.panelk.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
            self.panels.grid_remove()
            self.panelp.grid_remove()
        elif per == 2:
            self.panelp.grid(row=3, column=0, columnspan=1000, padx=1, pady=0)
            self.panelk.grid_remove()
            self.panels.grid_remove()
    def result(self):
        global name
        global vin
        global nich
        global los
        f = open('result.txt', 'a')  # открытие в режиме добавления
        f.write(name +"      "+ str(vin) +"     "+str(nich)+"     "+str(los)+"    "+ str(round((vin/(vin+los))*100,1))+"% "+"\n")  # запись  в файл
        f.close()  # закрытие файла
        self.destroy()
    def changePC(self,per):
        global vin
        global nich
        global los
        
        PK = random.randint(0, 2)
        Label1 = tk.Label(self, text=" ")
        Label1.grid_remove()
        if PK == 0:
            self.PKpanels.grid(row=3, column=4000)
            self.PKpanelk.grid_remove()
            self.PKpanelp.grid_remove()
            if per == 0:
                e = '  Ничья  '
                Label1 = tk.Label(self, text=e)
                nich+=1
            elif per == 2:
                e = ' Выиграл '
                Label1 = tk.Label(self, text=e)
                vin+=1
            elif per == 1:
                e = ' Проиграл '
                Label1 = tk.Label(self, text=e)
                los+=1
        elif PK == 1:
            self.PKpanelk.grid(row=3, column=4000)
            self.PKpanels.grid_remove()
            self.PKpanelp.grid_remove()
            if per == 1:
                e = '  Ничья  '
                Label1 = tk.Label(self, text=e)
                nich += 1
            elif per == 0:
                e = ' Выиграл '
                Label1 = tk.Label(self, text=e)
                vin += 1
            elif per == 2:
                e = ' Проиграл '
                Label1 = tk.Label(self, text=e)
                los += 1
        elif PK == 2:
            self.PKpanelp.grid(row=3, column=4000)
            self.PKpanelk.grid_remove()
            self.PKpanels.grid_remove()
            if per == 2:
                e = '  Ничья  '
                Label1 = tk.Label(self, text=e)
                nich += 1
            elif per == 1:
                e = ' Выиграл '
                Label1 = tk.Label(self, text=e)
                vin += 1
            elif per == 0:
                e = ' Проиграл '
                Label1 = tk.Label(self, text=e)
                los += 1

        Label1.grid(row=5, column=0)
def main():
    app = Demo1()
    app.title("Начало начал")
    app.geometry('300x200+200+100')
    app.mainloop()

if __name__ == '__main__':
    main()