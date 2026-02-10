#2daimensional DataFreme
import pandas as pd
data = {
    "name": ["raj", "keyur", "dev"],
    "rollno": [10,22,34],
    "isPresent": [True, False, True]
}
df = pd.DataFrame(data)

print(df)