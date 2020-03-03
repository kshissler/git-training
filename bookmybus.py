from threading import *

class BookMyBus:
	
	def __init__ (self, availableSeats):
		self.availableSeats = availableSeats
		self.l = Lock()
		
	def buy(self,seatsRequested):
		self.l.acquire()
		print(current_thread().getName(),"Number of seats currently available: ",self.availableSeats)
		if(self.availableSeats >= seatsRequested):
			print(current_thread().getName(),"Confirming a seat.")
			print(current_thread().getName(),"Processing the payment")
			print(current_thread().getName(),"Printing the Ticket.")
			self.availableSeats -= seatsRequested
		else:
			print("Sorry, No Seats available.")
		self.l.release()

obj = BookMyBus(10)

t1 = Thread(target = obj.buy, args = (3,))
t2 = Thread(target = obj.buy, args = (4,))
t3 = Thread(target = obj.buy, args = (3,))
t4 = Thread(target = obj.buy, args = (2,))

t1.start()
t2.start()
t3.start()
t4.start()
