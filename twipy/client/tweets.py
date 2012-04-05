from twipy.client import api_method

@api_method(
    path='/1/statuses/:id/retweeted_by',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def retweeted_by(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/:id/retweeted_by/ids',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def retweeted_by_ids(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweets/:id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def retweets(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/show/:id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='GET')
def show(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/destroy/:id',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def destroy(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweet/:id',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def retweet(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/update',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/update_with_media',
    subdomain='upload',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update_with_media(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/oembed',
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def oembed(client, **kwargs):
    pass