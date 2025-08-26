# 2.2. UPDATE AND DELETE SPECIFIC ELEMENTS

org_list = list(range(1,5))
print(len(org_list))

#update part
#First idx
org_list[0] = 12
print(f"Update first index, then list = {org_list}")

#idx'th element
org_list[2] = 65
print(f"Update 2nd index value, then list = {org_list}")

#last element
org_list[-1] = 98
print(f"Update last element in the list = {org_list}")


# delete by index
del org_list[1]
print(f"After delete first index value, the list: {org_list}")

# delete by value

print(f"Delete element 98 from list: { (org_list.remove(98) or True) if 98 in org_list else False }")
print(f"The list is: {org_list}")