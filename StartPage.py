import tkinter
import datetime
import sqlite3

class StartPage():
    def __init__(self):
        self.str = f"{datetime.datetime.now()} :  программа запущена\n"
        self.Start = tkinter.Tk()
        self.Start.geometry('640x500')  # геометрия окна
        self.Start.title("Программа для контроля веса")  # название окна
        self.Max()
        self.str += f"{datetime.datetime.now()} : вычислено значение максимального веса {self.max}\n"
        label3=tkinter.Label(self.Start, text=f"Максимальный вес за все время {self.max}", bg="lightgrey", fg="red")
        label3.place(x=100, y=250)
        self.str+=f"{datetime.datetime.now()} :  максимальный вес выведен на форму\n"
        self.Min()
        self.str += f"{datetime.datetime.now()} : вычислено значение минимального веса {self.min}\n"
        label4 = tkinter.Label(self.Start, text=f"Минимальный вес за все время {self.min}", bg="lightgrey", fg="green")
        label4.place(x=100, y=300)
        self.str += f"{datetime.datetime.now()} :  минимальный вес выведен на форму\n"
        label = tkinter.Label(self.Start, text="Введите ваш вес сейчас", bg="lightgrey", fg="red")
        label.place(x=100, y=50)
        self.message_entry = tkinter.Entry(self.Start, textvariable='')
        self.message_entry.place(x=300, y=50)
        btn1 = tkinter.Button(self.Start, text="Занести вес в базу", bg="lightgreen", fg="black",
                              command=self.ToBase)
        btn1.place(x=300, y=110)
        self.Start.mainloop()

    def ToBase(self):
        self.b = self.message_entry.get()
        self.str+=f"{datetime.datetime.now()} : получен вес {self.b}\n"
        if self.b.find(",")>1:
            self.str+=f"{datetime.datetime.now()} : найдедена запятая в позиции {self.b.find(',')}\n"
            self.b=self.b.replace(",",".")
            self.str = self.str + f"{datetime.datetime.now()} : заменена на точку, получено значение {self.b}\n"
        try:
         self.b1=float(self.b)
         self.str+=f"{datetime.datetime.now()} : вес успешно взять в работу \n"
        except ValueError:
            print("Ошибка значения")
            self.str+="Ошибка значения\n"
            self.Comment = tkinter.Toplevel(self.Start)
            self.Comment.geometry('400x200+200+200')
            self.Comment.title("Ошибка значения веса!")
            label = tkinter.Label(self.Comment, text="Введите Заново!", bg="lightgrey", fg="red")
            label.place(x=10, y=10)
            label = tkinter.Label(self.Comment, text="Нужно вводить дробное число!", bg="lightgrey", fg="red")
            label.place(x=10, y=30)
            label = tkinter.Label(self.Comment, text="Оно должно быть разделено точкой или запятой!", bg="lightgrey", fg="red")
            label.place(x=10, y=50)
            label = tkinter.Label(self.Comment, text="Пустым окно быть не должно!", bg="lightgrey",
                                  fg="red")
            label.place(x=10, y=70)
            btn2 = tkinter.Button(self.Comment, text="Исправить вес", bg="red", fg="black",
                                  command=lambda: self.Comment.destroy())
            btn2.place(x=10, y=150)
        else:
            self.Comment = tkinter.Toplevel(self.Start)
            self.Comment.geometry('300x200+200+200')
            self.Comment.title("Желаете ли внести комментарий?")
            label = tkinter.Label(self.Comment, text="Введите комментарий:", bg="lightgrey", fg="red")
            label.place(x=10, y=10)
            self.message_entry1 = tkinter.Entry(self.Comment, textvariable='')
            self.message_entry1.place(x=10, y=50,width=260,height=50)
            btn1 = tkinter.Button(self.Comment, text="Занести вес и комментарий в базу", bg="lightblue", fg="black",
                              command=self.SQLPower)
            btn1.place(x=10, y=120)
            btn2 = tkinter.Button(self.Comment, text="Передумал заносить", bg="red", fg="black",
                              command=lambda: self.Comment.destroy())
            btn2.place(x=10, y=150)
            self.str+=f"{datetime.datetime.now()} : вес внесен успешно {self.b}\n"

    def SQLPower(self):
        self.a= self.message_entry1.get()
        self.str+=f"{datetime.datetime.now()} : указан комментарий {self.a}\n"
        self.f = str(datetime.datetime.now())
        self.str+=f"{datetime.datetime.now()} : дата и время получены {self.f}\n"
        self.day=datetime.datetime.today().weekday()
        self.str += f"{datetime.datetime.now()} : день недели получен {self.day}\n"
        self.Comment.destroy()
        self.diff=float(self.max)-self.b1
        self.str += f"{datetime.datetime.now()} : разница в весе вычислена {self.diff}\n"
        btn2 = tkinter.Button(self.Start, text="Закрыть и покинуть", bg="red", fg="black",
                              command=lambda: self.Start.destroy())
        btn2.place(x=300, y=140)
        self.str += f"{datetime.datetime.now()} : Выполняется подключение к базе данных\n"
        mt = sqlite3.connect("Weight.bd")
        self.str += f"{datetime.datetime.now()} : База данных подключена\n"
        cursor = mt.cursor()
        self.str += f"{datetime.datetime.now()} : Курсор выставлен\n"
        cursor.execute('''Insert into Weight values (?,?,?,?,?);''',
                       (self.f, self.b1, self.a, self.day,self.diff))
        self.str += f"{datetime.datetime.now()} : Значения успешно переданы в базу данных \n"
        mt.commit()
        self.str += f"{datetime.datetime.now()} : Изменения сохранены \n"
        cursor = mt.cursor()
        self.str+=f"{datetime.datetime.now()} :База\n"
        for row in cursor.execute("select* from Weight"): self.str+=f"{row}\n"

    def Max(self):
        self.str += f"{datetime.datetime.now()} : Выполняется подключение к базе данных\n"
        mt = sqlite3.connect("Weight.bd")
        self.str += f"{datetime.datetime.now()} : База данных подключена\n"
        cursor = mt.cursor()
        self.str += f"{datetime.datetime.now()} : Курсор выставлен\n"
        for row in cursor.execute('''Select max (Weight) from Weight'''):
            row=str(row)
            self.max=row[1:6]

    def Min(self):
        self.str += f"{datetime.datetime.now()} : Выполняется подключение к базе данных\n"
        mt = sqlite3.connect("Weight.bd")
        self.str += f"{datetime.datetime.now()} : База данных подключена\n"
        cursor = mt.cursor()
        self.str += f"{datetime.datetime.now()} : Курсор выставлен\n"
        for row in cursor.execute('''Select min (Weight) from Weight'''):
            row=str(row)
            self.min=row[1:6]

    def __str__(self)-> str:
        return self.str