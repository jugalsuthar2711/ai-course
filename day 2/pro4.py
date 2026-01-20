"""
File:
Project:
Author:
Version:
Release Date:
"""
# sequential datatypes

"""
    1. List - []
        - mutable
        - any daatatype is supported

    2. Tuple - ()
        - immutable

    3. Set - {}
        - stores only unique values

    4. Dictonary 
        - mutable
        - {key: value}
"""

nums = [1,2,3]

cart = ["tablet", "books", 30, False, None, {1: "a"}, nums]

print(cart)

cart[0] = "laptop"

print(cart)
print(type(cart))

marks = (55,66,77,88,99)
print(marks)

# marks[0] = 60

# print(marks)
print(type(marks))