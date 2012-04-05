from twipy.client import api_method

@api_method(
    path='/1/help/test',
    subdomain='api',
    rate_limited=False,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def test(client, **kwargs):
    pass

@api_method(
    path='/1/help/configuration',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def configuration(client, **kwargs):
    pass

@api_method(
    path='/1/help/languages',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def languages(client, **kwargs):
    pass