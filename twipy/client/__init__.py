import urllib
import urllib2
from functools import wraps

def api_method(**meta):
    def api(method):
        @wraps(method)
        def wrapper(client, **kwargs):
            #TODO: replace path slots with params and pop them
            request = client.build_request(meta['path'], meta['subdomain'], 'json', meta['http_method'], kwargs)
            request.set_requires_authentication(meta['requires_authentication'])
            return request
        return wrapper
    return api