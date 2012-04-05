from twipy.client import api_method

@api_method(
    path='/1/users/lookup',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='POST')
def lookup(client, **kwargs):
    pass

@api_method(
    path='/1/users/profile_image/:screen_name',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def profile_image(client, **kwargs):
    pass

@api_method(
    path='/1/users/search',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def search(client, **kwargs):
    pass

@api_method(
    path='/1/users/show',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def show(client, **kwargs):
    pass

@api_method(
    path='/1/users/contributees',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def contributees(client, **kwargs):
    pass

@api_method(
    path='/1/users/contributors',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def contributors(client, **kwargs):
    pass