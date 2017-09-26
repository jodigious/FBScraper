#
# FBScrappy
#
# Developed by Josh Galvin
# @jodigious
# www.jodigious.com
# josh.galvin@jodigous.com
#

# Importing modules
import urllib2
import json
import datetime
import csv
import time

# Create application tokens
# I need to generate these with Facebook API Graph (how to automate...?)_
app_id = "1956308844643415"
app_secret = "xxxxxx"

access_token = app_id + "|" + app_secret

# Using NYTimes FB page for an example
page_id = 'nytimes'

def testFacebookPageData(page_id, access_token):

    # construct the URL
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve the data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = json.dumps(data, indent=4, sort_keys=True)

#testFacebookPageData(page_id, access_token)