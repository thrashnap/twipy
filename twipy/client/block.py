from twipy.client import api_method

@api_method(path='/1/blocks/blocking', response_formats=('json', 'xml'))
def blocking(client, **kwargs):
    pass

@api_method(path='/1/blocks/blockings/ids', response_formats=('json', 'xml'))
def blocking_ids(client, **kwargs):
    pass

@api_method(path='/1/blocks/exists', response_formats=('json', 'xml'))
def exists(client, **kwargs):
    pass

@api_method(path='/1/blocks/create', response_formats=('json', 'xml'), 
    http_method='POST')
def create(client, **kwargs):
    pass

@api_method(path='/1/blocks/destroy', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def destroy(client, **kwargs):
    pass
