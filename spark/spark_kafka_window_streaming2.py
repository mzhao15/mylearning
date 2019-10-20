
''' The inbound tweets are coming from an Apache Kafka topic. Any matched tweets will be sent to another 		Kafka topic. The match criteria are:

	1. Not a retweet
	2. Contains at least one URL
	3. URL(s) are not on a whitelist (for example, we're not interested in links to spotify.com, or back to twitter.com)
	4. The Tweet text must match at least two from a predefined list of artists, albums, and tracks. This is necessary to avoid lots of false positives - think of how many music tracks there are out there, with names that are common in English usage ("yesterday" for example). So we must match at least two ("Yesterday" and "Beatles", or "Yesterday" and "Help!").
		Match terms will take into account common misspellings (Little Mix -> Litle Mix), hashtags (Little Mix -> #LittleMix), etc 

	As well as matching the tweet against the above conditions, we will enrich the tweet message body to store the identified artist/album/track to support subsequent downstream processing.

	The final part of the requirement is to keep track of the number of inbound tweets, the number of matched vs unmatched, and for those matched, which artists they were for. These counts need to be per batch and over a window of time too.'''





