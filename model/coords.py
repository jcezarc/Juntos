from model.base_model import Model

class Coords(Model):
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude
