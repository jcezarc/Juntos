import requests
from service.db.loader import Loader

class JsonLoader(Loader):
    def download_file(self, url):
        res = requests.get(url)
        return res.json()['results']

    @staticmethod
    def flatten(source, prefix=''):
        result = {}
        for key, value in source.items():
            if isinstance(value, dict):
                result.update(
                    JsonLoader.flatten(value, prefix+key+'__')
                )
            else:
                result[prefix+key] = value
        return result
    
    def process_record(self, record):
        record = JsonLoader.flatten(record)
        super().process_record(record)
    