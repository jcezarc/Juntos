import sys
sys.path.append('..')
from model.base_model import Model

class CustomerModel(Model):
    def __init__(self, name, gender, location, phone, picture, user_type):
        self.name = name
        self.gender = gender[0].upper()
        self.location = location
        self.phone = phone
        self.picture = picture
        self.type = user_type
