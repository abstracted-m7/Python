# 2.1. APPEND() AND INSERT() OPERATIONS

org_num_list = list(range(1,5))

appd_list = org_num_list.copy()
appd_list.append(15)

isrt_list = appd_list.copy()
isrt_list.insert(0,123)

print(f"Original list: {org_num_list}")
print(f"After append list is: {appd_list}")
print(f"After insert 123 in idx 0, list is: {isrt_list}")
