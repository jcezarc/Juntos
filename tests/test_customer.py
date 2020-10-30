import sys
sys.path.append('..')
from service.customer import CustomerService
from service.db.fake_loader import FakeLoader
from service.db.loader import Loader

FakeLoader('')

def test_filter_region():
    service = CustomerService()
    res, status_code = service.find({
        'region': 'NW'
    })
    assert status_code == 200
    users = res['users']
    expected = {
            "name": {
                "first": "Sofia",
                "last": "Barbosa",
                "title": "miss"
            },
            "gender": "F",
            "phone": "+55 7819707",
        }
    assert users[1]['name'] == expected['name']
    assert users[1]['phone'] == expected['phone']

def get_compare_user():
    return {
        "name": {
            "first": "Leandro",
            "last": "Costela",
            "title": "mr"
        },
        "gender": "M",
        "location": {
            "coords": {
                "latitude": -48.52416057042378,
                "longitude": -21.76564042586542
            },
            "street": "Alameda Luiz Felipe Sales, 698",
            "city": "Martins",
            "state": "MT",
            "postcode": "15210-745"
        },
        "phone": "+55 2119013175",
        "picture": {
            "large": "https://da.com/LeandroCostela/large.png",
            "medium": "https://da.com/LeandroCostela/medium.jpg",
            "thumbnail": "https://da.com/LeandroCostela/thumbnail.gif"
        },
        "type": "ESPECIAL"
    }

def test_filter_type():
    service = CustomerService()
    res, status_code = service.find({
        'type': 'ESPECIAL',
        'pageNumber': 2
    })
    user = res['users'][0]
    expected = get_compare_user()
    assert user == expected

def test_pagination():
    service = CustomerService()
    res, status_code = service.find({
        'region': 'S',
        'pageNumber': 3
    }) # ==> http://localhost:5000/juntos/customer?region=S&pageNumber=3
    expected = {
        "pageNumber": 3,
        "pageSize": 10,
        "totalCount": 21,
        "users": [
            get_compare_user()
        ]
    }
    assert res == expected
