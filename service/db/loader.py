from service.location import region, type_by_location, FIELD_LAT, FIELD_LON
from model.customer import CustomerModel
from model.location import Location
from model.picture import Picture
from model.coords import Coords
from model.phone import Phone
from model.name import Name

class FilterException(Exception):
    pass

class Loader:
    data  = []
    filtered = None

    def __init__(self, url):
        for record in self.download_file(url):
            self.process_record(record)
        self.filtered = None

    @classmethod
    def filter(cls, region, user_type):
        if region is None and user_type is None:
            raise FilterException()
        result = []
        for d in cls.data:
            if region and region not in d['region'] \
            or user_type and user_type != d['type']:
                continue
            result.append(d)
        cls.filtered = result

    def download_file(self):
        raise NotImplementedError('Método "download_file" não implementado na classe {}!'.format(
            self.__class__.__name__
        ))

    def process_record(self, record):
        params = (
            float(record[FIELD_LAT]),
            float(record[FIELD_LON]),
        )
        record['region'] = region(params)
        record['type'] = type_by_location(params)
        Loader.data.append(record)

    @classmethod
    def fetch_one(cls, index):
        if index >= cls.record_count():
            return None
        d = cls.filtered[index]
        model = CustomerModel(
            Name(
                d['name__first'],
                d['name__last'],
                d['name__title'],
            ),
            d['gender'],
            Location(
                d['location__street'],
                d['location__city'],
                d['location__state'],
                d['location__postcode'],
                Coords(
                    d[FIELD_LAT],
                    d[FIELD_LON],
                )
            ),
            Phone(d['phone']),
            Picture(
                d['picture__large'],
                d['picture__medium'],
                d['picture__thumbnail'],
            ),
            d['type']
        )
        return model.transform()

    @classmethod
    def record_count(cls):
        return len(cls.filtered)
