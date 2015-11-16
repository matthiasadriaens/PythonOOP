from consumption import consumption

class cafe:

	consumptions = []
	def __init__(self,info):
		self.info = info

	def order(self,consumption,quantity):
		if quantity == 1:
			print str(quantity) + " %s is ordered in the " % consumption.name + self.info
		else:
			print str(quantity) + " %s are ordered in the " % consumption.name + self.info
		amount_to_pay = str(quantity*consumption.price)
		print "The amount to pay equals %s" % amount_to_pay 

	def add_consumption(self,consumption):
		self.consumptions.append(consumption)

	def get_consumptions(self):
		return self.consumptions

	def __repr__(self):
		return self.consumptions

if __name__ == "__main__":
	ybeer = consumption("beer",2.67)
	yucca = cafe("yucca")
	yucca.add_consumption(ybeer)
	yucca.order(ybeer,35)
	print yucca.consumptions





