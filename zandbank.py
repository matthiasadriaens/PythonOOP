from consumption import consumption
from bediende import bediende

class cafe:

	def __init__(self,info):
		self.info = info
		self.consumptions = []
		self.employees = []

	def order(self,consumption,quantity):
		if quantity == 1:
			print str(quantity) + " %s is ordered in the " % consumption.name + self.info
		else:
			print str(quantity) + " %s are ordered in the " % consumption.name + self.info
		amount_to_pay = str(quantity*consumption.price)
		print "The amount to pay equals %s" % amount_to_pay 

	def add_bediend(self,bediende):
		self.employees.append(bediende)

	def add_consumption(self,consumption):
		self.consumptions.append(consumption)

	def get_consumptions(self):
		return self.consumptions

	def get_employees(self):
		return self.employees



if __name__ == "__main__":
	yucca = cafe("yucca")
	ybeer = consumption("beer",2.67)
	yucca.add_consumption(ybeer)
	marloes = bediende("Marloes de hete poes",10.7)
	print marloes.hourpay
	print yucca.consumptions

