from model.base_model import Model

class Name(Model):
	def __init__(self, first, last, _title):
		self.first = first.title()
		self.last = last.title()
		self.title = _title
	def __str__(self):
		return '{} {} {}'.format(self.title, self.first, self.last)
