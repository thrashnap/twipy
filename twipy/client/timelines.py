from twipy.client import api_method

@api_method(path='/1/statuses/home_timeline')
def home_timeline(client, **kwargs):
    pass

@api_method(path='/1/statuses/mentions')
def mentions(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweeted_by_me', 
    response_formats=('json', 'xml', 'atom'))
def retweeted_by_me(client, **kwargs):
    pass
        
@api_method(path='/1/statuses/retweeted_to_me', 
    response_formats=('json', 'xml', 'atom'))
def retweeted_to_me(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweeted_of_me', 
    response_formats=('json', 'xml', 'atom'))
def retweets_of_me(client, **kwargs):
    pass

@api_method(path='/1/statuses/user_timeline', 
    requires_authentication='supported')
def user_timeline(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweeted_to_user', 
    requires_authentication='supported', response_formats=('json', 'xml'))
def retweeted_to_user(client, **kwargs):
    pass

@api_method(path='/1/statuses/retweeted_by_user', rate_limited=False, 
    requires_authentication='supported', response_formats=('json', 'xml'))
def retweeted_by_user(client, **kwargs):
    pass