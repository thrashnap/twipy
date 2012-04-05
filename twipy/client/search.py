from twipy.client import api_method

@api_method(path='/search', subdomain='search',
    requires_authentication='no', response_formats=('json', 'atom'))
def search(client, **kwargs):
    pass
