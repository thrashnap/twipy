from twipy.client import api_method

@api_method(
    path='/1/followers/ids',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def followers_ids(client, **kwargs):
    pass

@api_method(
    path='/1/friends/ids',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def friends_ids(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/exists',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def friendships_exists(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/incoming',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def friendships_incoming(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/outgoing',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def frienships_outgoing(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/show',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def friendships_show(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/create',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def friendships_create(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/destroy',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def friendships_destroy(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/lookup',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def friendships_lookup(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/update',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def friendships_update(client, **kwargs):
    pass

@api_method(
    path='/1/friendships/no_retweet_ids',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def friendships_no_retweet_ids(client, **kwargs):
    pass