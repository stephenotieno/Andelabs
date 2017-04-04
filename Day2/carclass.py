class Car(object):
	def _init_(self, vehicle, model = 'GM', name = 'General'):
		self.type = vehicle
		self.model = model
		self.name = name

	def saloon_car(self):
		if self.vehicle is 'trailer':
			return True
		else:
			return False