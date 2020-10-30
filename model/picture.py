from model.base_model import Model

class Picture(Model):
	def __init__(self, large, medium, thumbnail):
		self.large = large
		self.medium = medium
		self.thumbnail = thumbnail
