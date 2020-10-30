from model.base_model import Model

class Location(Model):
    def __init__(self, street, city, state, postcode, coords):
        self.coords = coords
        self.street = street
        self.city = city
        self.state = state
        self.postcode = postcode
