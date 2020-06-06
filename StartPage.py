import tkinter
import datetime
import sqlite3

class StartPage():
    def __init__(self):
        self.str="программа запущена\n"
        self.Start = tkinter.Tk()
        self.Start.geometry('640x500')  # геометрия окна
        self.Start.title("Программа для контроля веса")  # название окна
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
        self.str+=f"получен вес {self.b}\n"
        if self.b.find(",")>1:
            self.str+=f"найдедена запятая в позиции {self.b.find(',')}\n"
            self.b=self.b.replace(",",".")
            self.str = self.str + f"заменена на точку, получено значение {self.b}\n"
        try:
         self.b1=float(self.b)
         self.str+=f"вес успешно взять в работу \n"
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
            self.str+=f"вес внесен успешно {self.b}\n"

    def SQLPower(self):
        self.a= self.message_entry1.get()
        self.str+=f"указан комментарий {self.a}\n"
        self.f = str(datetime.datetime.now())
        self.str+=f"дата и время получены {self.f}\n"
        self.Comment.destroy()
        self.str += f"Выполняется подключение к базе данных\n"
        mt = sqlite3.connect("Weight.bd")
        self.str += f"База данных подключена\n"
        cursor = mt.cursor()
        self.str += f"Курсор выставлен\n"
        cursor.execute('''Insert into Weight values (?,?,?);''',
                       (self.f, self.b1, self.a))
        self.str += f"Значения успешно переданы в базу данных \n"
        mt.commit()
        self.str += f"Изменения сохранены \n"

    def __str__(self)-> str:
        return self.str