from twipy.client import api_method

@api_method(
    path='/1/notifications/follow',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def follow(client, **kwargs):
    pass

@api_method(
    path='/1/notifications/leave',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def leave(client, **kwargs):
    pass