import tkinter
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
        self.Comment = tkinter.Toplevel(self.Start)
        self.Comment.geometry('300x200+200+200')
        self.Comment.title("Желаете ли внести комментарий?")
        label = tkinter.Label(self.Comment, text="Введите комментарий:", bg="lightgrey", fg="red")
        label.place(x=10, y=10)
        self.message_entry = tkinter.Entry(self.Comment, textvariable='')
        self.message_entry.place(x=10, y=50,width=260,height=50)
        btn1 = tkinter.Button(self.Comment, text="Занести вес и комментарий в базу", bg="lightblue", fg="black",
                              command=self.SQLPower)
        btn1.place(x=10, y=120)
    def SQLPower(self):pass