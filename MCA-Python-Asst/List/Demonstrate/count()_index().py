# 4.3. TUPLE METHODS: count() and index()
org_tup = (1, 2, 3, 2, 4, 2, 5, 3, 6, 2, 7)

#count
counts = {num: org_tup.count(num) for num in set(org_tup)}
print(f"Numbers repetation - {counts}")


#index()
# Finding first occurrence index
index_2 = org_tup.index(2)
index_3 = org_tup.index(3)

print(f"First index of 2: {index_2}")
print(f"First index of 3: {index_3}")