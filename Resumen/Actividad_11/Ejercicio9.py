from collections import defaultdict
import threading

documents = [
    "hello world",
    "hello",
    "hello mapreduce world",
    "mapreduce in python",
    "hello mapreduce"
]

def map_function(doc):
    words = doc.split()
    return [(word, 1) for word in words]

def reduce_function(word, counts):
    return (word, sum(counts))

mapped = []
for doc in documents:
    mapped.extend(map_function(doc))

shuffled = defaultdict(list)
for word, count in mapped:
    shuffled[word].append(count)

reduced = []
for word, counts in shuffled.items():
    reduced.append(reduce_function(word, counts))

for word, count in reduced:
    print(f"{word}: {count}")
