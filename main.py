from tkinter import *
from parking_garage import *

garage = Garage()

root = Tk()
root.title("Parking Garage")
root.option_add("*font", "tkDefaultFont 40")
feedback = Text()
take = Button(root, text="Take Ticket", command=lambda: garage.take_ticket())
take.pack()
pay = Button(root, text="Pay for Parking", command=lambda: garage.pay_for_parking())
pay.pack()
leave = Button(root, text="Leave Garage", command=lambda: garage.leave_garage())
leave.pack()
root.mainloop()