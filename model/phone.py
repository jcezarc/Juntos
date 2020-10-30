from model.base_model import Model

class Phone(Model):
    def __init__(self, phone_number):
        only_digits = lambda s: ''.join(filter(str.isdigit, s))
        elements = phone_number.split(')')
        if len(elements) > 1:            
            self.area_code = only_digits(elements[0])
            phone_number = elements[-1]            
        else:
            self.area_code = ''
        self.country = '55'
        self.phone_number = only_digits(phone_number)
    def transform(self):
        return '+{} {}{}'.format(
            self.country,
            self.area_code,
            self.phone_number
        )
