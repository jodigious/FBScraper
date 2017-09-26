#
# FBScrappy
#
# Plagerized (lol) by Josh Galvin, aka this is not original work
# @jodigious
# www.jodigious.com
# josh.galvin@jodigous.com
#

# Importing modules
import urllib2
import json
import datetime
import time

# Create application tokens (using facebook for developers app)
app_id = "1956308844643415"
app_secret = "__CHANGEME__"     # This should be cleared OFTEN (and never stored if possible).
                                                    # It might be good practice to clear between commits.

access_token = app_id + "|" + app_secret        # This can be generated also through Facebook Graph API.
                                                # https://developers.facebook.com/tools/explorer/
# Using NYTimes FB page for an example
page_id = 'nytimes'
print "page_id = %s" % page_id

# Basic function to construct the URL and start scraping.
def testFacebookPageData(page_id, access_token):

    # Construct the URL
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/feed"
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    print "URL = %s" % url

    # Catches errors and waits
    request_until_succeed(url)

    # Retrieve the data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())

    print "data retrieved, dumping..."
    print json.dumps(data, indent=4, sort_keys=True)        # Prints to console the data.
    with open('%s.json' % page_id, 'w') as f:                    # Saves to json file.
        json.dump(data, f)

# Simple helper function to catch errors (i.e., any HTTP SEO != 200) and tries again
def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    response = urllib2.urlopen(req)

    while success is False:
        try:
            if response.getcode() == 200:
                success = True
                print "HTTP Status = 200"
        except Exception, e:
            print e
            time.sleep(5)
            print "Error for URL %s: %s" % (url, datetime.datetime.now())

    return response.read()

testFacebookPageData(page_id, access_token)
