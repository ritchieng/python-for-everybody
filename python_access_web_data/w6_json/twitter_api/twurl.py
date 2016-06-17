# File for twtest.py to import to get post data

import urllib
import oauth
# Fill in the application's information in hidden
import hidden

# How to do OAuth signing
def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, 
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


def test_me():
    print '* Calling Twitter...'
    # Count: # of post to load
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'drchuck', 'count': '2'} )
    print url
    connection = urllib.urlopen(url)

    # Gets the body
    # JSON
    data = connection.read()
    print data

    # Gets dictionary of headers
    # JSON
    headers = connection.info().dict
    print headers
