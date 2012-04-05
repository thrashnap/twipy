from twipy.client import api_method

@api_method(
    path='/1/saved_searches',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def saved_searches(client, **kwargs):
    pass

@api_method(
    path='/1/saved_searches/show/:id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def show(client, **kwargs):
    pass

@api_method(
    path='/1/saved_searches/create',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def create(client, **kwargs):
    pass

@api_method(
    path='/1/saved_searches/destroy/:id',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass