from twipy.client import api_method

@api_method(path='/1/users/lookup', requires_authentication='supported',
    response_formats=('json', 'xml'), http_method='POST')
def lookup(client, **kwargs):
    pass

@api_method(path='/1/users/profile_image/:screen_name', 
    requires_authentication='no', response_formats=('json', 'xml'))
def profile_image(client, **kwargs):
    pass

@api_method(path='/1/users/search', response_formats=('json', 'xml'))
def search(client, **kwargs):
    pass

@api_method(path='/1/users/show', requires_authentication='supported',
    response_formats=('json', 'xml'))
def show(client, **kwargs):
    pass

@api_method(path='/1/users/contributees', requires_authentication='supported',
    response_formats=('json', 'xml'))
def contributees(client, **kwargs):
    pass

@api_method(path='/1/users/contributors', requires_authentication='supported',
    response_formats=('json', 'xml'))
def contributors(client, **kwargs):
    pass
