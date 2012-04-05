from twipy.client import api_method

@api_method(
    path='/1/lists/all',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def all(client, **kwargs):
    pass

@api_method(
    path='/1/lists/statuses',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml', 'atom'),
    http_method='GET')
def statuses(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members/destroy',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def members_destroy(client, **kwargs):
    pass

@api_method(
    path='/1/lists/memberships',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def memberships(client, **kwargs):
    pass

@api_method(
    path='/1/lists/subscribers',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def subscribers(client, **kwargs):
    pass

@api_method(
    path='/1/lists/subscribers/create',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def subscribers_create(client, **kwargs):
    pass

@api_method(
    path='/1/lists/subscribers/show',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def subscribers_show(client, **kwargs):
    pass

@api_method(
    path='/1/lists/subscribers/destroy',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def subscribers_destroy(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members/create_all',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def members_create_all(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members/show',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def members_show(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def members(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members/create',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def members_create(client, **kwargs):
    pass

@api_method(
    path='/1/lists/destroy',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(
    path='/1/lists/update',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update(client, **kwargs):
    pass

@api_method(
    path='/1/lists/create',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def create(client, **kwargs):
    pass

@api_method(
    path='/1/lists',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def lists(client, **kwargs):
    pass

@api_method(
    path='/1/lists/show',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def lists_show(client, **kwargs):
    pass

@api_method(
    path='/1/lists/subscriptions',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def subscriptions(client, **kwargs):
    pass

@api_method(
    path='/1/lists/members/destroy_all',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def members_destroy_all(client, **kwargs):
    pass