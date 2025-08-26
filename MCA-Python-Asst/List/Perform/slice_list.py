# 2.4. LIST SLICING OPERATIONS

org_list = list(range(1,20))

#first 5 element slice
first_five_element = org_list[:5]

#last 5 element slice
last_five_element = org_list[-5:]

#every second element
every_second = org_list[::2]

#every second element satrting from idx 1
first_to_two = org_list[1::2]

#ELement from idx 2 to 7
idx_two_to_seven = org_list[2:8]


#print all above
print(f"First 5 element: {first_five_element}")
print(f"Last 5 element: {last_five_element}")
print(f"Every second element: {every_second}")
print(f"Every second element starting from index 1: {first_to_two}")
print(f"Elements from index 2 to 7: {idx_two_to_seven}")


