from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["Austria Belgium Austria","Belgium Belgium Austria"]

cv = CountVectorizer()

count_matrix = cv.fit_transform(text)
print (count_matrix.toarray())

similarity_scores = cosine_similarity(count_matrix)
print (similarity_scores)