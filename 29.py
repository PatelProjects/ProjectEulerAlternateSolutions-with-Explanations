# Unlike arrays, sets cannot contain duplicates, so we an use a set to automatically filter out these duplicate terms

terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b)
        
print(len(terms))
