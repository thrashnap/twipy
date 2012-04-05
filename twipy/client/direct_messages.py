from twipy.client import api_method

@api_method(
    path='/1/direct_messages',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def direct_messages(client, **kwargs):
    pass

@api_method(
    path='/1/direct_messages/sent',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def sent(client, **kwargs):
    pass

@api_method(
    path='/1/direct_messages/destroy/:id',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(
    path='/1/direct_messages/new',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def new(client, **kwargs):
    pass

@api_method(
    path='/1/direct_messages/show/:id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def show(client, **kwargs):
    pass