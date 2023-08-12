# # code 1

# # import pandas as pd
# # from sklearn.datasets import load_iris
# # from sklearn.cluster import KMeans
# # from sklearnex  import patch_sklearn

# # patch_sklearn()

# # # Load the iris dataset
# # iris = load_iris()
# # X = iris.data

# # # Use the Intel optimized version of KMeans
# # kmeans = KMeans(
# #     algorithm="full",
# #     n_clusters=3,
# #     init="k-means++",
# #     n_init=10,
# #     max_iter=300,
# #     tol=0.0001,
# #     precompute_distances="auto",
# #     verbose=0,
# #     random_state=None,
# #     copy_x=True,
# #     n_jobs=None,
# # )

# # # Fit the KMeans model to the iris data
# # kmeans.fit(X)

# # # Predict the clusters for the iris data
# # y_pred = kmeans.predict(X)

# # # Add the predicted cluster labels to the iris dataset
# # iris_df = pd.DataFrame(X, columns=iris.feature_names)
# # iris_df["Cluster"] = y_pred

# # # Print the first 5 rows of the dataset with cluster labels
# # print(iris_df.head())

# # Code no 5
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import ElasticNet
# from sklearn.metrics import r2_score
# from sklearn.utils import shuffle
# from sklearnex import patch_sklearn

# # Load the iris dataset
# iris = datasets.load_iris()
# X, y = iris.data, iris.target

# # Shuffle the data
# X, y = shuffle(X, y, random_state=0)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Enable Intel Optimization for Scikit-Learn
# patch_sklearn()

# # Initialize the ElasticNet model with Intel Optimization
# enet = ElasticNet(
#     alpha=1.0,
#     l1_ratio=0.5,
#     fit_intercept=True,
#     normalize=False,
#     precompute=False,
#     max_iter=1000,
#     copy_X=True,
#     tol=0.0001,
#     warm_start=False,
#     positive=False,
#     random_state=0,
#     selection="cyclic",
# )

# # Fit the model to the training data
# enet.fit(X_train, y_train)

# # Predict the target values of the testing data
# y_pred = enet.predict(X_test)

# # Calculate the R2 score of the model
# r2 = r2_score(y_test, y_pred)

# print("R2 score:", r2)


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from map import Axes3D
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Apply KMeans clustering algorithm
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

# Add the cluster labels to the dataset
df["cluster"] = kmeans.labels_

# Plot the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    df["sepal length (cm)"],
    df["sepal width (cm)"],
    df["petal length (cm)"],
    c=df["cluster"],
)
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
plt.show()


import array as np

np.array.flattened(order="c")
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
Print(arr)
flat_array = arr.flattened()
Print("1d numpy Array:")
Print(flate_array)


def flatten_2d_array(arr):
    flattened_arr = []
    for row in arr:
        flattened_arr += row
    return flattened_arr


# Example usage
two_d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_d_array = flatten_2d_array(two_d_array)
print(one_d_array)


import array as arr

myarray = arr.array("i", [])
n = int(input("How many elemnts you want ? : "))
for i in range(n):
    value = int(input("Enter the elements :  "))
    myarray.append(value)
print("Now the array is : \n", myarray)
