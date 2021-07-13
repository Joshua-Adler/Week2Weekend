from tkinter.messagebox import showinfo

class Garage():

	tickets = []
	parking_spaces = [i for i in range(1, 21)]
	current_ticket = {}

	def take_ticket(self):
		if len(self.parking_spaces) == 0:
			showinfo("Error", "This parking garage is full.")
		else:
			if self.current_ticket:
				self.tickets.append(self.current_ticket)
			self.current_ticket = {}
			self.current_ticket['space'] = self.parking_spaces.pop()
			showinfo("Success!", f"Your parking space is #{self.current_ticket['space']}.")
			
		

	def pay_for_parking(self):
		if not self.current_ticket:
			showinfo("Error", "You can not pay for a ticket that you have not taken.")
		elif 'paid' in self.current_ticket:
			showinfo("Error", "You have already paid for your ticket.")
		else:
			showinfo("Success!", "Payment complete. You have 15 minutes to leave.")
			self.current_ticket['paid'] = True
		

	def leave_garage(self):
		if not self.current_ticket:
			showinfo("Error", "You are not in the parking garage.")
		elif 'paid' in self.current_ticket:
			showinfo("Bye!", "Have a nice day.")
			self.parking_spaces.append(self.current_ticket['space'])
			if len(self.tickets) > 0:
				self.current_ticket = self.tickets.pop()
			else:
				self.current_ticket = {}
		else:
			showinfo("Error", "You are trapped here until you pay.")
			
	
