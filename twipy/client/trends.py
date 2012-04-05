from twipy.client import api_method

@api_method(
    path='/1/trends/:woeid',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def trends(client, **kwargs):
    pass

@api_method(
    path='/1/trends/available',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def available(client, **kwargs):
    pass

@api_method(
    path='/1/trends/daily',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def daily(client, **kwargs):
    pass

@api_method(
    path='/1/trends/weekly',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json'),
    http_method='GET')
def weekly(client, **kwargs):
    pass