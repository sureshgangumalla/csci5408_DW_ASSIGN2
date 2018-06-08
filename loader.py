
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
actions = []
print("loading into elasticsearch database begins")
with open('processed.csv', 'r') as readfile:
	reader = csv.DictReader(readfile)
	for row in reader:
		action = {
        	         "_index": "csci5408_a2",
                         "_type": "tweets",
			 "doc_type" : "docs",
                         "_source": {
                              "tweets": str(row['tweet']),
			      "sentiment": str(row['sentiment']),
			      "sentiment_score": float(row['sentiment_score'])
	                 }
        	}
		actions.append(action)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
helpers.bulk(es, actions)
print("loaded into elasticsearch database")
