# -*- coding: utf-8 -*-

import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from pattern.en import sentiment
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="MJZOyGbqqHirJZoVLt4hwr5QY"
csecret="V20ReBIC36u5r0ZliBHiwKZlgjZCruOWdu0JvFvp3ocI8WZN0u"
atoken="2688211724-ZUx3d7F8g2db5m9whvSFWjvHGgoZvYBFkCjBLcu"
asecret="hvVhARsXgfnk21uXpP7kZWaOO9fOZfFodiBIvJrwHMqt5"

class listener(StreamListener):
	def on_data(self, data):
		try:
			all_data = json.loads(data)
			tweet = all_data["text"]
			print "[Tweet]:\n%s"%self.tweet
			print "\n[By]: %s"%all_data["user"]["screen_name"]
			print "---------------"
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
