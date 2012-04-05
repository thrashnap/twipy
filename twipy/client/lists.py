from twipy.client import api_method

@api_method(path='/1/lists/all', requires_authentication='supported',
    response_formats=('json', 'xml'))
def all(client, **kwargs):
    pass

@api_method(path='/1/lists/statuses', requires_authentication='supported',
    response_formats=('json', 'xml', 'atom'))
def statuses(client, **kwargs):
    pass

@api_method(path='/1/lists/members/destroy', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def members_destroy(client, **kwargs):
    pass

@api_method(path='/1/lists/memberships', requires_authentication='supported',
    response_formats=('json', 'xml'))
def memberships(client, **kwargs):
    pass

@api_method(path='/1/lists/subscribers', requires_authentication='supported',
    response_formats=('json', 'xml'))
def subscribers(client, **kwargs):
    pass

@api_method(path='/1/lists/subscribers/create', 
    response_formats=('json', 'xml'), http_method='POST')
def subscribers_create(client, **kwargs):
    pass

@api_method(path='/1/lists/subscribers/show', response_formats=('json', 'xml'))
def subscribers_show(client, **kwargs):
    pass

@api_method(path='/1/lists/subscribers/destroy', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def subscribers_destroy(client, **kwargs):
    pass

@api_method(path='/1/lists/members/create_all', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def members_create_all(client, **kwargs):
    pass

@api_method(path='/1/lists/members/show', response_formats=('json', 'xml'))
def members_show(client, **kwargs):
    pass

@api_method(path='/1/lists/members', requires_authentication='supported',
    response_formats=('json', 'xml'))
def members(client, **kwargs):
    pass

@api_method(path='/1/lists/members/create', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def members_create(client, **kwargs):
    pass

@api_method(path='/1/lists/destroy', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(path='/1/lists/update', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def update(client, **kwargs):
    pass

@api_method(path='/1/lists/create', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def create(client, **kwargs):
    pass

@api_method(path='/1/lists', requires_authentication='supported',
    response_formats=('json', 'xml'))
def lists(client, **kwargs):
    pass

@api_method(path='/1/lists/show', requires_authentication='supported', 
    response_formats=('json', 'xml'))
def lists_show(client, **kwargs):
    pass

@api_method(path='/1/lists/subscriptions',
    requires_authentication='supported', response_formats=('json', 'xml'))
def subscriptions(client, **kwargs):
    pass

@api_method(path='/1/lists/members/destroy_all', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def members_destroy_all(client, **kwargs):
    pass
