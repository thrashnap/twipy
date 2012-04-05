from twipy.client import api_method

@api_method(path='/1/report_spam', rate_limited=False,
    response_formats=('json', 'xml'), http_method='POST')
def report_spam(client, **kwargs):
    pass
