class Model:
    def transform(self):
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Model):
                value = value.transform()
            result[key] = value
        return result
