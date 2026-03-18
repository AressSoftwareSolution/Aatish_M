import pickle

data = {"name": "Rahul", "age": 25}

with open("pickle_example.pkl", "wb") as f:
    pickle.dump(data, f)

with open("pickle_example.pkl", "rb") as f:
    loaded = pickle.load(f)
