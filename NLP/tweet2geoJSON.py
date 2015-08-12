"""
SCHEME:

{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [-122.09,37.64 ]
  },
  "properties": {
    "name": "@BrianLehman",
    "tweet_body": "I freaking love maps!",
  }
}
"""

def format2geoJSON(tweet):
	if tweet["geo"] != 'null':
		# get lat,lng and create geoJSON object:
		tweet_geoJSON = {
						  "type": "Feature",
						  "geometry": {
						    "type": "Point",
						    "coordinates": tweet['geo'] #[lat,lng]
						  },
						  "properties": {
						    "name": tweet['user']['screen_name'],
						    "tweet_body": tweet['text'],
						  }
						}
		return tweet_geoJSON


	elif tweet["place"] != 'null':
		# convert place to lat,lng and create geoJSON object: 
		tweet_geoJSON = {
						  "type": "Feature",
						  "geometry": {
						    "type": "Point",
						    "coordinates": tweet['geo'] #[lat,lng]
						  },
						  "properties": {
						    "name": tweet['user']['screen_name'],
						    "tweet_body": tweet['text'],
						  }
						}
		return ""


	else: return ""
