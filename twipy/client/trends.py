from twipy.client import api_method

@api_method(path='/1/trends/:woeid', requires_authentication='no',
    response_formats=('json'))
def trends(client, **kwargs):
    pass

@api_method(path='/1/trends/available', requires_authentication='no',
    response_formats=('json', 'xml'))
def available(client, **kwargs):
    pass

@api_method(path='/1/trends/daily', requires_authentication='no',
    response_formats=('json'))
def daily(client, **kwargs):
    pass

@api_method(path='/1/trends/weekly', requires_authentication='no',
    response_formats=('json'))
def weekly(client, **kwargs):
    pass
