from twipy.client import api_method

@api_method(
    path='/1/favorites',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def favorites(client, **kwargs):
    pass

@api_method(
    path='/1/favorites/create/:id',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def create(client, **kwargs):
    pass

@api_method(
    path='/1/favorites/destroy/:id',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass