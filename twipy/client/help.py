from twipy.client import api_method

@api_method(path='/1/help/test', rate_limited=False,
    requires_authentication='no', response_formats=('json', 'xml'))
def test(client, **kwargs):
    pass

@api_method(path='/1/help/configuration',
    requires_authentication='no', response_formats=('json', 'xml'))
def configuration(client, **kwargs):
    pass

@api_method(path='/1/help/languages',
    requires_authentication='no', response_formats=('json', 'xml'))
def languages(client, **kwargs):
    pass
