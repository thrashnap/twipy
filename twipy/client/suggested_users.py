from twipy.client import api_method

@api_method(
    path='/1/users/suggestions',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def suggestions(client, **kwargs):
    pass

@api_method(
    path='/1/users/suggestions/:slug',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def suggestions_slug(client, **kwargs):
    pass

@api_method(
    path='/1/users/suggestions/:slug/members',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def suggestions_slug_members(client, **kwargs):
    pass