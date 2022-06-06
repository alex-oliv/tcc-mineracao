from collections import Counter
import json
from pprint import pprint

with open('logs.txt') as infile:
    data = (json.loads(line) for line in infile)
    counter = Counter((row['type'], row['key']) for row in data)

pprint(dict(counter))