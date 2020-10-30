from service.location import region, type_by_location

def test_region():
    params = (50, 84)
    expected = 'NE'
    assert region(params) == expected
    params = (-50, -84)
    expected = 'SW'
    assert region(params) == expected

def test_user_type():
    expected = 'TRABALHOSO'
    user_type = type_by_location((0, 0))
    assert user_type == expected
    expected = 'ESPECIAL'
    user_type = type_by_location((-48, -20))
    assert user_type == expected
    expected = 'NORMAL'
    user_type = type_by_location((-50, -30))
    assert user_type == expected
