'''
Este arquivo NÃO faz parte do projeto,
sendo usado apenas uma vez para gerar
os dados fictícios necessários para os 
testes unitários.
'''
import random
from faker import Faker
#     ^------- Não está em requirements.txt (!)
import sys
sys.path.append('..')
from service.location import FIELD_LAT, FIELD_LON, location_by_type


def fake_records(target):
    fake = Faker('pt_BR')
    result = []
    get_names = {
        'female': lambda: [fake.first_name_female(), fake.last_name_female(), random.choice(['mrs', 'miss'])],
        'male': lambda: [fake.first_name_male(), fake.last_name_male(), 'mr']
    }
    is_laborious = True
    while len(result) < target:
        d = {}
        gender = random.choice(['male', 'female'])
        name = get_names[gender]()
        d['name__title'] = name.pop()
        d['name__first'] = name[0]
        d['name__last'] = name[-1]
        d['gender'] = gender
        addr = fake.address().split('\n')
        d['location__street'] = addr[0]
        addr = addr[-1].split(' ')
        d['location__postcode'] = addr[0]
        d['location__city'] = addr[1]
        d['location__state'] = addr[-1]
        if is_laborious:
            d[FIELD_LAT], d[FIELD_LON] = fake.latlng()
        else:
            curr_type = random.choice(['ESPECIAL', 'NORMAL'])
            d[FIELD_LAT], d[FIELD_LON] = location_by_type(curr_type)
        is_laborious = not is_laborious
        d['phone'] = fake.phone_number()[4:]
        url = fake.url()+''.join(name)+'/'
        d['picture__large'] = url+'large.png'
        d['picture__medium'] = url+'medium.jpg'
        d['picture__thumbnail'] = url+'thumbnail.gif'
        result.append(d)
    return result

if __name__ == '__main__':
    print(fake_records(30))
