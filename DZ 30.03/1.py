from collections import Counter

w=input("введите слово")
c = Counter(w)

print(c.most_common(1)[0][0])
