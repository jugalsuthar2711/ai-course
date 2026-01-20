person = {
    "firstname": "xyz",
    "middlename": "abc",
    "lastname": "pqr",
    "parents": {
        "father":{
            "name": "nnnn"
        },
        "mother":{
            "name": "mmmm"
        }
    },
    "qualifications": ["SSC", "HSC", "BCA","MCA"],
    "hobbies": {"music,watching-movies,reading-novels/books"},
    "isAlive": True
}

print(person)
print(person["isAlive"])

person["isAlive"] = False
print(person["isAlive"])

#message of person variable
print(type(person))