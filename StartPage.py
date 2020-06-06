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
        btn6 = tkinter.Button(self.Start, text="Занести вес в базу", bg="lightgreen", fg="black",
                              command=self.ToBase)
        btn6.place(x=300, y=110)
        self.Start.mainloop()
    def ToBase(self):pass