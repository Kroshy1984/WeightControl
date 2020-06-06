import tkinter
import datetime

class StartPage():
    def __init__(self):
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
        print(self.b.find(","))
        if self.b.find(",")>1:self.b=self.b.replace(",",".")
        print(self.b)
        try:
         self.b1=float(self.b)
        except ValueError:
            print("Ошибка значения")
            self.Comment = tkinter.Toplevel(self.Start)
            self.Comment.geometry('300x200+200+200')
            self.Comment.title("Ошибка значения")
            label = tkinter.Label(self.Comment, text="Введите Заново!", bg="lightgrey", fg="red")
            label.place(x=10, y=10)
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

    def SQLPower(self):
        self.a= self.message_entry1.get()
        self.f = str(datetime.datetime.now())
        print(self.f)
        print(self.a)

    def __str__(self)-> str:
        return f"то, что ушло в базу - {self.f,self.a}"