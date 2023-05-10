"""
I'm making a function to calculate a dot product when given two vectors. The code is later used in a matrix multiplication function. The issue I'm having is that the parameters passed in from the matrix multiplication function are 1x3 matrices that in order to multiply together, I need to use dot+=A[0,,i]*B[0,i]. The submission website expects dot+=A[i],B[i] and I'm not sure how to get my matrices converted to arrays. Picture of my two functions

I tried recreating the matrices and isolating rows but I still had [[1,2,3]] come up and mes with my dot product function.

"""


def dot_product(a, b):
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
    return dot


def multiply_dataframes(df1, df2):
    # convert dataframes to numpy matrices
    mat1 = df1.values
    mat2 = df2.values
    # perform matrix multiplication
    result = np.matmul(mat1, mat2)
    # return as a DataFrame
    return pd.DataFrame(result)


"""
I suggest you to use the numpy library to perform matrix multiplication. 

You can use the `numpy.matmul` function to perform matrix multiplication. Read more about it here: https://numpy.org/doc/stable/reference/generated/numpy.matmul.html

You can also use the numpy.dot function to perform dot product. Read more about it here: https://numpy.org/doc/stable/reference/generated/numpy.dot.html

Here is an example of how to use the numpy library to perform matrix multiplication:
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.matmul(a, b)

print(c)


"""
But if you want to perform matrix multiplication without using the numpy library, you can use the following code:
"""

def multiply_dataframes(df1, df2):
    # convert dataframes to numpy matrices
    mat1 = df1.values
    mat2 = df2.values
    # perform matrix multiplication
    result = np.matmul(mat1, mat2)
    # return as a DataFrame
    return pd.DataFrame(result)