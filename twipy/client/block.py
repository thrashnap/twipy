from twipy.client import api_method

@api_method(
    path='/1/blocks/blocking',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def blocking(client, **kwargs):
    pass

@api_method(
    path='/1/blocks/blockings/ids',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def blocking_ids(client, **kwargs):
    pass

@api_method(
    path='/1/blocks/exists',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def exists(client, **kwargs):
    pass

@api_method(
    path='/1/blocks/create',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def create(client, **kwargs):
    pass

@api_method(
    path='/1/blocks/destroy',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass