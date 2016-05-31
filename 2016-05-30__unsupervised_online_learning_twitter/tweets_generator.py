# -*- coding: utf-8 -*-

import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from pattern.en import sentiment
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret : get yours with twitter API
ckey="XXX"
csecret="XXX"
atoken="XXX"
asecret="XXX"

class listener(StreamListener):
	def on_data(self, data):
		try:
			all_data = json.loads(data)
			tweet = all_data["text"]
			print "[Tweet]:\n%s"%tweet
			print "\n[By]: %s"%all_data["user"]["screen_name"]
			print "[Polarity]: %s"%sentiment(tweet)[0]
			print "[Subjectivity]: %s"%sentiment(tweet)[1]
			print "---------------"
			time.sleep(1)
		except Exception,e:
			print str(e)
			return(True)

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

while(True):
	try:
	    twitterStream = Stream(auth, listener())
	    twitterStream.filter(track=["Trump"],languages=["en"])
	except Exception,e:
	    print str(e)
