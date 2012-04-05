from twipy.client import api_method

@api_method(path='/1/followers/ids',
    requires_authentication='supported', response_formats=('json', 'xml'))
def followers_ids(client, **kwargs):
    pass

@api_method(path='/1/friends/ids',
    requires_authentication='supported', response_formats=('json', 'xml'))
def friends_ids(client, **kwargs):
    pass

@api_method(path='/1/friendships/exists',
    requires_authentication='supported', response_formats=('json', 'xml'))
def friendships_exists(client, **kwargs):
    pass

@api_method(path='/1/friendships/incoming', response_formats=('json', 'xml'))
def friendships_incoming(client, **kwargs):
    pass

@api_method(path='/1/friendships/outgoing', response_formats=('json', 'xml'))
def frienships_outgoing(client, **kwargs):
    pass

@api_method(path='/1/friendships/show',
    requires_authentication='supported', response_formats=('json', 'xml'))
def friendships_show(client, **kwargs):
    pass

@api_method(path='/1/friendships/create', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def friendships_create(client, **kwargs):
    pass

@api_method(path='/1/friendships/destroy', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def friendships_destroy(client, **kwargs):
    pass

@api_method(path='/1/friendships/lookup', response_formats=('json', 'xml'))
def friendships_lookup(client, **kwargs):
    pass

@api_method(path='/1/friendships/update', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def friendships_update(client, **kwargs):
    pass

@api_method(path='/1/friendships/no_retweet_ids', 
    response_formats=('json', 'xml'))
def friendships_no_retweet_ids(client, **kwargs):
    pass
