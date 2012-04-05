from twipy.client import api_method

@api_method(
    path='/search',
    subdomain='search',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'atom'),
    http_method='GET')
def search(client, **kwargs):
    pass