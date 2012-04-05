from twipy.client import api_method

@api_method(
    path='/1/account/rate_limit_status',
    subdomain='api',
    rate_limited=False,
    requires_authentication='supported',
    response_formats=('json', 'xml'),
    http_method='GET')
def rate_limit_status(client, **kwargs):
    pass

@api_method(
    path='/1/account/verify_credentials',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def verify_credentials(client, **kwargs):
    pass

@api_method(
    path='/1/account/end_session',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def end_session(client, **kwargs):
    pass

@api_method(
    path='/1/account/update_profile',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update_profile(client, **kwargs):
    pass

@api_method(
    path='/1/account/update_profile_background_image',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update_profile_background_image(client, **kwargs):
    pass

@api_method(
    path='/1/account/update_profile_colors',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update_profile_colors(client, **kwargs):
    pass

@api_method(
    path='/1/account/update_profile_image',
    subdomain='api',
    rate_limited=False,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='POST')
def update_profile_image(client, **kwargs):
    pass

@api_method(
    path='/1/account/totals',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def totals(client, **kwargs):
    pass

@api_method(
    path='/1/account/settings',
    subdomain='api',
    rate_limited=True,
    requires_authentication='yes',
    response_formats=('json', 'xml'),
    http_method='GET')
def settings(client, **kwargs):
    pass

@api_method(
    path='/1/account/settings',
    subdomain='api',
    rate_limited=False,
    requires_authentication='no',
    response_formats=('json', 'xml'),
    http_method='POST')
def settings_update(client, **kwargs):
    pass