from twipy.client import api_method

@api_method(path='/1/statuses/:id/retweeted_by', 
    requires_authentication='supported', response_formats=('json', 'xml'))
def retweeted_by(client, **kwargs):
    pass

@api_method(path='/1/statuses/:id/retweeted_by/ids', 
    response_formats=('json', 'xml'))
def retweeted_by_ids(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweets/:id', response_formats=('json', 'xml'))
def retweets(client, **kwargs):
    pass

@api_method(path='/1/statuses/show/:id', requires_authentication='no',
    response_formats=('json', 'xml'))
def show(client, **kwargs):
    pass

@api_method(path='/1/statuses/destroy/:id', response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweet/:id', response_formats=('json', 'xml'),
    http_method='POST')
def retweet(client, **kwargs):
    pass

@api_method(path='/1/statuses/update', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def update(client, **kwargs):
    pass

@api_method(path='/1/statuses/update_with_media', subdomain='upload',
    response_formats=('json', 'xml'), http_method='POST')
def update_with_media(client, **kwargs):
    pass

@api_method(path='/1/statuses/oembed', requires_authentication='supported',
    response_formats=('json', 'xml'))
def oembed(client, **kwargs):
    pass
