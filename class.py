class Car(object):
	def  __init__(self,model,color,company,speed_limit):
		self.color=color
		self.model=model
		self.company=company
		self.speed_limit=speed_limit

	def start(self):
		print("started")

	def stop(self):
		print("stopped")

	def accelerate(self):
		print("accelerating")
		"accelerator functionality here"

	def change_gear(self,gear_type):
		print("gear changed")
		"gear related functionality here"




