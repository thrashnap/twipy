from twipy.client import api_method

@api_method(path='/1/legal/privacy',
    requires_authentication='no', response_formats=('json', 'xml'))
def privacy(client, **kwargs):
    pass

@api_method(path='/1/legal/tos',
    requires_authentication='no', response_formats=('json', 'xml'))
def tos(client, **kwargs):
    pass
