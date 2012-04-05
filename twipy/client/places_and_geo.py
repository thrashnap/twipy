from twipy.client import api_method

@api_method(path='/1/geo/id/:place_id', requires_authentication='no',
    response_formats=('json'))
def id(client, **kwargs):
    pass

@api_method(path='/1/geo/reverse_geocode', requires_authentication='no',
    response_formats=('json'))
def reverse_geocode(client, **kwargs):
    pass

@api_method(path='/1/geo/search', requires_authentication='no',
    response_formats=('json'))
def search(client, **kwargs):
    pass

@api_method(path='/1/geo/similar_places', requires_authentication='no',
    response_formats=('json'))
def similar_places(client, **kwargs):
    pass

@api_method(path='/1/geo/place', response_formats=('json'),
    http_method='POST')
def place(client, **kwargs):
    pass
