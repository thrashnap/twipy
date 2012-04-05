import urllib
import urllib2
from functools import wraps

def api_method(path, subdomain='api', rate_limited=True, 
    requires_authentication='yes', 
    response_formats=('json', 'xml', 'rss', 'atom'), http_method='GET'):
    def api(method):
        @wraps(method)
        def wrapper(client, **kwargs):
            #TODO: replace path slots with params and pop them
            request = client.build_request(path, subdomain, 'json', http_method, kwargs)
            request.set_requires_authentication(requires_authentication)
            return request
        return wrapper
    return api