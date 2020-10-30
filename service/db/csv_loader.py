import requests
import csv
from service.db.loader import Loader

class CsvLoader(Loader):

    field_list = None

    def download_file(self, url):
        res = requests.get(url)
        content = res.content.decode('utf-8-sig')
        cr = csv.reader(content.splitlines(), delimiter=',')
        return list(cr)

    @classmethod
    def inflate(cls, source):
        result = {}
        for key, value in zip(cls.field_list, source):
            result[key] = value
        return result

    def process_record(self, record):
        if not CsvLoader.field_list:
            CsvLoader.field_list = record
            return
        record = CsvLoader.inflate(record)
        super().process_record(record)
