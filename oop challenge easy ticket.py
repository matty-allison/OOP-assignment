from tkinter import *
root = Tk()
root.title("Ticket Sales")
root.geometry("600x700")
root.config(bg="#8C1586")
class TicketSales:
    canvas = Canvas(root, width = 150, height = 150)
    canvas.place(x= 200, y=40)
    img = PhotoImage(file="ticket.png")
    canvas.create_image(75,75, image=img)
    price_calculation = StringVar()
    results = StringVar()
    def __init__(self, master):
        self.cellphonelabel = Label(master, text="Enter your cellphone number")
        self.cellphonelabel.place(x=30, y=350)
        self.cellnum_entry = Entry(master, width=30)
        self.cellnum_entry.place(x=250, y=350)
        self.ticketlabel = Label(master, text="Select a ticket catergory")
        self.ticketlabel.place(x=30, y=400)
        OptionList = ["Soccer", "Movies", "Theatre"]
        variable = StringVar(master)
        variable.set(OptionList[0])
        self.opt = OptionMenu(master, variable, *OptionList)
        self.opt.place(x=250, y=400)
        self.opt.config(width=5)
        self.num_of_tickets = Label(master, text="How many tickets do you want?")
        self.num_of_tickets.place(x=30, y=470)
        self.numbers = Spinbox(master, width=5, from_=0, to= 10)
        self.numbers.place(x=250, y=470)
        self.btn = Button(master, text="Final Price", command=self.finalprice)
        self.btn.place(x=30, y=500)
        self.price = Label(master, text=" ", width=50, textvariable=self.results)
        self.price.place(x=30, y=550)
        self.clear = Button(master, text="Clear info", command=self.clearbtn)
        self.clear.place(x=250, y=500)

    def clearbtn(self):
        self.cellnum_entry.delete(0, END)
        self.opt.option_clear()
        self.numbers.delete(0, END)

    def finalprice(self):
        cal_soccer = int(self.numbers.get()) * 40 + 0.14 * 40
        self.results.set(cal_soccer)
        cal_movies = int(self.numbers.get()) * 75 + 0.14 * 75
        self.results.set(cal_movies)
        cal_theatre = int(self.numbers.get()) * 100 + 0.14 * 100
        self.results.set(cal_theatre)


x = TicketSales(root)
root.mainloop()
