# -*- coding: utf-8 -*-
import jsonpickle
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tweets = list(open('jstweets.json','rt'))
count=0
i=0
f = csv.writer(open("test.csv", "wb+"))
f.writerow(["Tweet", "Verified User", "Location"])
for t in tweets:
	t = json.loads(t)
	try:
		if(t['place']) is not None:
			if((t['place']['name'].split()[0]).lower()) == 'kansas':
    				f.writerow([t['text'],t['user']['verified'],t['place']['name']])
				i=i+1
				count=count+1
	except KeyError:
		pass
print 'Tweets with  kansas city  as loc:'
print count
