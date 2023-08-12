# Q. Section C

# Q.1 len() method
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print("Total sets : ", len(arr))
print("Total elements is: ", arr.size)

# Q.2 str.replace() method
my_string = "My name are MANISH GIRI."
new_string = my_string.replace("are", "is")
print(new_string)

# Q.3 str.join() method
# i)
words = ["My", "name", "is", "MANISH", "GIRI"]
a = " "
my_string = a.join(words)
print(my_string)
# ii)
a = ["m", "a", "n", "i", "s", "h"]
b = "~"
m = b.join(a)
print(m)

# Q.4 np.random.randint() method
# (start,end,form of matrix size)
random_array = np.random.randint(0, 100, size=(5, 5))
print(random_array)

# Q.5 np.random.rand() method
# (size of matrix , elements in a row)
random_array = np.random.rand(3, 5)
print(random_array)

# Q.6 np.sort() method
# np.sort(a, axis=-1, kind=None, order=None)
# column-wise high value to low value sorting
a = np.array([[4.1, 1.2, 3.4], [6.5, 1.1, 2.2], [2.3, 9.8, 4.5]])
sorted_array = np.sort(a, axis=0)[::-1]
print(sorted_array)

# Q.7 np.argsort() method
# np.argsort(a, axis=-1, kind=None, order=None)

print("Jani naaaaaaaaaaaaaa")

# Q.8 array.copy() method
a = np.array([1, 2, 3])
b = a.copy()
print(b)

# Q.9 array.reshape() method
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape((3, 2))
print(b)

# Q.10 np.argmin() method
print("Jani naaaaaaaa.")
