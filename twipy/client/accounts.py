from twipy.client import api_method

@api_method(path='/1/account/rate_limit_status', rate_limited=False,
    requires_authentication='supported', response_formats=('json', 'xml'))
def rate_limit_status(client, **kwargs):
    pass

@api_method(path='/1/account/verify_credentials', 
    response_formats=('json', 'xml'))
def verify_credentials(client, **kwargs):
    pass

@api_method(path='/1/account/end_session', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def end_session(client, **kwargs):
    pass

@api_method(path='/1/account/update_profile', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def update_profile(client, **kwargs):
    pass

@api_method(path='/1/account/update_profile_background_image', 
    rate_limited=False, response_formats=('json', 'xml'), http_method='POST')
def update_profile_background_image(client, **kwargs):
    pass

@api_method(path='/1/account/update_profile_colors', rate_limited=False, 
    response_formats=('json', 'xml'), http_method='POST')
def update_profile_colors(client, **kwargs):
    pass

@api_method(path='/1/account/update_profile_image', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def update_profile_image(client, **kwargs):
    pass

@api_method(path='/1/account/totals', response_formats=('json', 'xml'))
def totals(client, **kwargs):
    pass

@api_method(path='/1/account/settings', response_formats=('json', 'xml'))
def settings(client, **kwargs):
    pass

@api_method(path='/1/account/settings', rate_limited=False,
    requires_authentication='no', response_formats=('json', 'xml'), 
    http_method='POST')
def settings_update(client, **kwargs):
    pass
