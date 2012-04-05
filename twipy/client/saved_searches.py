from twipy.client import api_method

@api_method(path='/1/saved_searches', response_formats=('json', 'xml'))
def saved_searches(client, **kwargs):
    pass

@api_method(path='/1/saved_searches/show/:id', response_formats=('json', 'xml'))
def show(client, **kwargs):
    pass

@api_method(path='/1/saved_searches/create', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def create(client, **kwargs):
    pass

@api_method(path='/1/saved_searches/destroy/:id', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def destroy(client, **kwargs):
    pass
