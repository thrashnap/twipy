from twipy.client import api_method

@api_method(path='/1/users/suggestions', requires_authentication='no',
    response_formats=('json', 'xml'))
def suggestions(client, **kwargs):
    pass

@api_method(path='/1/users/suggestions/:slug', requires_authentication='no',
    response_formats=('json', 'xml'))
def suggestions_slug(client, **kwargs):
    pass

@api_method(path='/1/users/suggestions/:slug/members', 
    requires_authentication='no', response_formats=('json', 'xml'))
def suggestions_slug_members(client, **kwargs):
    pass
