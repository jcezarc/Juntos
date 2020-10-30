'''
Serviços de geolocalização

ATENÇÃO:
São cálculos simplificados.
Não levam em contra trigonometria, curvatura da Terra etc.
'''

import math

FIELD_LAT = 'location__coordinates__latitude'
FIELD_LON = 'location__coordinates__longitude'

USER_TYPES = {
	'ESPECIAL': [
		{
			'minlon': -2.196998,
			'minlat': -46.361899,
			'maxlon': -15.411580,
			'maxlat': -34.276938
		},
		{
			'minlon': -19.766959,
			'minlat': -52.997614,
			'maxlon': -23.966413,
			'maxlat': -44.428305
			}
	],
	'NORMAL': [{
		'minlon': -26.155681,
		'minlat': -54.777426,
		'maxlon': -34.016466,
		'maxlat': -46.603598
	}]
}


def region(params):
	positions = {
		'N': lambda lat, lon: lat >= 0,
		'S': lambda lat, lon: lat < 0,
		'E': lambda lat, lon: lon >= 0,
		'W': lambda lat, lon: lon < 0,
	}
	result = ''
	for key, is_valid in positions.items():
		if is_valid(*params):
			result += key
	return result

def type_by_location(params):
	def fits(lat, lon, minlon, minlat, maxlon, maxlat):
		if minlon > maxlon:
			lon, minlon, maxlon = -lon, -minlon, -maxlon
		latOK = lat >= minlat and lat <= maxlat
		lonOK = lon >= minlon and lon <= maxlon
		return latOK and lonOK
	for key, array in USER_TYPES.items():
		for values in array:
			if fits(*params, **values):
				return key
	return 'TRABALHOSO'

def location_by_type(type):
	def mid(min, max):
		sign = abs(min)/min
		return math.sqrt(min*max) * sign
	def get_point_in(minlon, minlat, maxlon, maxlat):
		lat = mid(minlat, maxlat)
		lon = mid(minlon, maxlon)
		return lat, lon
	params = USER_TYPES[type][-1]
	return get_point_in(**params)
