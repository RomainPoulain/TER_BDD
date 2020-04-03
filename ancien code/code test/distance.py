import nltk
w1 = 'mapping'
w2 = 'mappings45'
print(nltk.edit_distance(w1, w2))


# technique 2

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))
list1 = ['dog', 'cat', 'cat', 'rat']
list2 = ['dog', 'cat', 'mouse']
print(jaccard_similarity(list1, list2))

# technique 3

mistake = "ligting"

words = ['apple', 'bag', 'drawing', 'listing', 'linking', 'living', 'lighting', 'orange', 'walking', 'zoo']

for word in words:
    ed = nltk.edit_distance(mistake, word)
    print(word, ed)
