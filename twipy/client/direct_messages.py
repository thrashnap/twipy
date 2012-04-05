from twipy.client import api_method

@api_method(path='/1/direct_messages')
def direct_messages(client, **kwargs):
    pass

@api_method(path='/1/direct_messages/sent')
def sent(client, **kwargs):
    pass

@api_method(path='/1/direct_messages/destroy/:id', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(path='/1/direct_messages/new', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def new(client, **kwargs):
    pass

@api_method(path='/1/direct_messages/show/:id',
    response_formats=('json', 'xml'))
def show(client, **kwargs):
    pass
