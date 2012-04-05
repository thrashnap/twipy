from twipy.client import api_method

@api_method(
    path='/1/statuses/home_timeline',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def home_timeline(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/mentions', 
    subdomain='api',
    rate_limited=True, 
    requires_authentication='yes',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def mentions(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweeted_by_me', 
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'atom'),
    http_method='GET')
def retweeted_by_me(client, **kwargs):
    pass
        
@api_method(
    path='/1/statuses/retweeted_to_me', 
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'atom'),
    http_method='GET')
def retweeted_to_me(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweeted_of_me', 
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml', 'atom'),
    http_method='GET')
def retweets_of_me(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/user_timeline', 
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml', 'rss', 'atom'),
    http_method='GET')
def user_timeline(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweeted_to_user', 
    subdomain='api',
    rate_limited=True,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def retweeted_to_user(client, **kwargs):
    pass

@api_method(
    path='/1/statuses/retweeted_by_user', 
    subdomain='api',
    rate_limited=False,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def retweeted_by_user(client, **kwargs):
    pass