from .Config import ACTIVECAMPAIGN_URL, ACTIVECAMPAIGN_API_KEY
from .ActiveCampaign import ActiveCampaign
import json
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error


class Contact(ActiveCampaign):

    def __init__(self, url, api_key):
