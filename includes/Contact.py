from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from .ActiveCampaign import ActiveCampaign
import json
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error


class Contact(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def add(self, params, post_data):
        request_url = '%s&api_action=contact_add&api_output=%s' % (self.url, self.output)
        if params:
            request_url = '%s&%s' % (request_url, params)
        post_data = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(request_url, post_data)
        response = json.loads(urllib.request.urlopen(req).read())
        return response

