from twipy.client import api_method

@api_method(
    path='/1/legal/privacy',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def privacy(client, **kwargs):
    pass

@api_method(
    path='/1/legal/tos',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def tos(client, **kwargs):
    pass