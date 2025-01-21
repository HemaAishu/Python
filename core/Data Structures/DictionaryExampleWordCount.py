sentence="hello world hello all hello world"
counts={}
for word in sentence.split():
    counts[word]=counts.get(word,0)+1
print(counts) # Output : {'hello': 3, 'world': 2, 'all': 1}