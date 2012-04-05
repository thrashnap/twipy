from twipy.client import api_method

@api_method(
    path='/1/geo/id/:place_id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def id(client, **kwargs):
    pass

@api_method(
    path='/1/geo/reverse_geocode',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def reverse_geocode(client, **kwargs):
    pass

@api_method(
    path='/1/geo/search',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def search(client, **kwargs):
    pass

@api_method(
    path='/1/geo/similar_places',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def similar_places(client, **kwargs):
    pass

@api_method(
    path='/1/geo/place',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json'),
    http_method='POST')
def place(client, **kwargs):
    pass