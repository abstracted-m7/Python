# Mixed nested tuples

nested_mixed = ((1, "a"), (2.5, "b", True), (3, "c", [1, 2]))
print(f"Mixed nested tuple: {nested_mixed}")
for i, inner_tuple in enumerate(nested_mixed):
    print(f"  Inner tuple {i}: {inner_tuple}")
    for j, item in enumerate(inner_tuple):
        print(f"    Element {j}: {item} ({type(item).__name__})")