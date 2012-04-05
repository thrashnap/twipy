from twipy.client import api_method

@api_method(path='/1/favorites')
def favorites(client, **kwargs):
    pass

@api_method(path='/1/favorites/create/:id', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def create(client, **kwargs):
    pass

@api_method(path='/1/favorites/destroy/:id', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def destroy(client, **kwargs):
    pass
