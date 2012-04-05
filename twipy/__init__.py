import urllib
import urllib2
from twipy.utils import importlib

class TwipyException(Exception):
    pass

class TwipyRequest(urllib2.Request):

    def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False):
        urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)

    def set_requires_authentication(self, requires_authentication=True):
        self.requires_authentication = requires_authentication

    def process():
        raise NotImplementedError()

class Method(object):

    def __init__(self, client, method_name):
        self.client = client
        self.method_name = method_name

    def __getattr__(self, key):
        return Method(self.client, '.'.join((self.method_name, key)))

    def __call__(self, **kwargs):
        try:
            dot = self.method_name.rindex('.')
            lib = importlib.import_module(self.method_name[:dot])
            method = getattr(lib, self.method_name[dot+1:])
            return method(self.client, **kwargs)
        except (ImportError, AttributeError):
            raise TwipyException("No such method") 
    
class Twipy(object):

    def __init__(self, host='twitter.com', secure=True):
        self.host = host
        self.protocol = 'https' if secure else 'http'
        self.opener = urllib2.OpenerDirector()

    def __getattr__(self, key):
        return Method(self, 'twipy.client.%s' % key)
        
    def build_request(self, path, subdomain='api', format='json', http_method='GET', params={}):
        url = '%s://%s.%s%s.%s' % (self.protocol, subdomain, self.host, path, format)
        data = urllib.urlencode(params)
        if http_method == 'GET':
            url = '%s?%s' % (url, data)
            data = None
        url = url.encode('utf-8')
        request = TwipyRequest(url, data)
        return request